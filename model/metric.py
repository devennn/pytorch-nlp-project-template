import torch


def accuracy(outputs, labels):
    """
    Compute the accuracy, given the outputs and labels for all tokens. Exclude PADding terms.

    Args:
        outputs: (np.ndarray) dimension batch_size*seq_len x num_tags - log softmax output of the model
        labels: (np.ndarray) dimension batch_size x seq_len where each element is either a label in
                [0, 1, ... num_tag-1], or -1 in case it is a PADding token.

    Returns: (float) accuracy in [0,1]
    """
    # pdb.set_trace()
    _, predicted = torch.max(outputs.data, 1)
    if len(labels.shape) > 1:
        _, labels = torch.max(labels.data, 1)
    total = len(labels)
    correct = (predicted == labels).sum()
    accuracy = float(correct) / total
    return accuracy
