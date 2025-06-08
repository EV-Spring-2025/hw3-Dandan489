[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SdXSjEmH)
# EV-HW3: PhysGaussian

This homework is based on the recent CVPR 2024 paper [PhysGaussian](https://github.com/XPandora/PhysGaussian/tree/main), which introduces a novel framework that integrates physical constraints into 3D Gaussian representations for modeling generative dynamics.

You are **not required** to implement training from scratch. Instead, your task is to set up the environment as specified in the official repository and run the simulation scripts to observe and analyze the results.


## Getting the Code from the Official PhysGaussian GitHub Repository
Download the official codebase using the following command:
```
git clone https://github.com/XPandora/PhysGaussian.git
```


## Environment Setup
Navigate to the "PhysGaussian" directory and follow the instructions under the "Python Environment" section in the official README to set up the environment.


## Running the Simulation
Follow the "Quick Start" section and execute the simulation scripts as instructed. Make sure to verify your outputs and understand the role of physics constraints in the generated dynamics.


## Homework Instructions
Please complete Part 1–2 as described in the [Google Slides](https://docs.google.com/presentation/d/13JcQC12pI8Wb9ZuaVV400HVZr9eUeZvf7gB7Le8FRV4/edit?usp=sharing).

## Homework Report
### Part 1
The videos are provided in `baseline_videos` <br>
You can also watch them on Youtube
- [sand](https://youtube.com/watch/vrjo0ci_WS8?feature=share)
- [jelly](https://youtube.com/watch/vrjo0ci_WS8?feature=share)

### Part 2
### Ablation Study
For the ablation study, I adjusted n_grid, substep_dt, grid_v_damping_scale, and softening, each time I increase or decrease the value of one parameter and keep the rest the same. <br>
The full PSNR score compared with the original video can be found in `wolf_{subject}`
#### n_grid (2 * particle_filling_n_grid):
> **original**: 200 <br>
**increased**: 300 ([youtube link](https://youtube.com/watch/uYEO_Bvy4qQ?feature=share)) <br>
average PSNR score: 25.17  <br>
**decreased**: 50 ([youtube link](https://youtube.com/watch/0fH_-jMTCs4?feature=share)) <br>
average PSNR score: 21.50 

#### substep_dt:
> **original**: 2e-5 <br>
**increased**: 4e-5 ([youtube link](https://youtube.com/watch/7eGOrnu2YnM?feature=share)) <br>
average PSNR score: 32.52 <br>
**decreased**: 1e-5 ([youtube link](https://youtube.com/watch/SFtJJVIJA-g?feature=share)) <br>
average PSNR score: 32.32

#### grid_v_damping_scale:
> **original**: 1.1 <br>
**increased**: 1.2 ([youtube link](https://youtube.com/watch/BpPif5dXkSQ?feature=share))<br>
average PSNR score: 69.14 <br>
**decreased**: 0.9 ([youtube link](https://youtube.com/watch/iVK-sbV8I1M?feature=share)) <br>
average PSNR score: 22.16

#### softening:
> **original**: 0.1 <br>
**increased**: 1.0 ([youtube link](https://youtube.com/watch/5lgQFTI70zc?feature=share)) <br>
average PSNR score: 68.94 <br>
**decreased**: 0.01 ([youtube link](https://youtube.com/watch/VjsKZRTmWGA?feature=share)) <br>
average PSNR score: 68.82 

### Takeaways & Findings
- **n_grid:** A smaller n_grid reduces the time needed, but decreases output quality and particle count, and increasing n_grid does the otherwise. Both of them significantly changes the output video, which can easily be seen visually and also shown by the very low PSNR score.
- **substep_dt:** A smaller substep should improves the simulation quality with the cost of taking longer to run, and from the PSNR score, it did change the output. However, I cannot see significant difference visually (higer PSNR score). 
- **grid_v_damping_scale:** Since the original damping scale is greater than 1, slightly increasing it does not make a difference. However, changing it to a value smaller than 1 causes the simulation to break down — the sand particles no longer fall. The deviation makes the PSNR score very low.
- **softening:** Changing the stress softening factor does not seem to affect the final result here, probably due to it being less important for the material that I chose.

### Bonus
To generate the appropriate parameters for arbitrary target materials, the most straightforward way is to train a model that can infer it automatically. The basic way with supervised learning is to learn from existing hand-crafted parameters with the material, a text description or the output video they represent, but this requires lots of human-made data. Another way is to let the model run the generated parameters in a simulation environment, and compared it with real life or ground truth video (or text description), then design a training loop that allows the model to gradually learn how to identify the best parameters that can fit the provided video (or text description). This way we do not have to manually set up parameters for all the data.

# Reference
```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```
