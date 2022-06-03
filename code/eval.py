import numpy as np

def reconstructionError(predicted_joints, gt_joints): 
  errors = []
  for pj in predicted_joints:
    e = np.linalg.norm(gt_joints - pj, axis=1).min()
    errors.append(e)
  error = np.mean(errors)
  
  return error