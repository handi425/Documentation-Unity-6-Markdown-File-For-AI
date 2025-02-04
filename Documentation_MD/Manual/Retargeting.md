[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Retargeting.html)
  * [中文](/cn/current/Manual/Retargeting.html)
  * [日本語](/ja/current/Manual/Retargeting.html)
  * [한국어](/kr/current/Manual/Retargeting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Retargeting.html)
  * [中文](/cn/current/Manual/Retargeting.html)
  * [日本語](/ja/current/Manual/Retargeting.html)
  * [한국어](/kr/current/Manual/Retargeting.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Humanoid Avatar](AvatarCreationandSetup.html)
  * Retarget Humanoid animations

[](AvatarCreationandSetup.html)

Humanoid Avatar

[](InverseKinematics.html)

Inverse Kinematics

# Retarget Humanoid animations

One of the most powerful features of Mecanim is the ability to retarget
**humanoid animations** An animation using humanoid skeletons. Humanoid models
generally have the same basic structure, representing the major articulate
parts of the body, head and limbs. This makes it easy to map animations from
one humanoid skeleton to another, allowing retargeting and inverse kinematics.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation). This means that you can
apply the same set of animations to different character models.
**Retargeting** is only possible for humanoid models with a configured
**Avatar** An interface for retargeting animation from one rig to another.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar). A configured avatar provides a the
ability to correspondence between the models’ bone structure.

## Recommended Hierarchy structure

When working with Mecanim animations, you can expect your **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) to contain the following elements:

  * The Imported character model, which has an Avatar on it.
  * The **Animator Component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent), referencing an **Animator
Controller** Controls animation through Animation Layers with Animation State
Machines and Animation Blend Trees, controlled by Animation Parameters. The
same Animator Controller can be referenced by multiple models with Animator
components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) asset.

  * A set of **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip), referenced from the Animator
Controller.

  * **Scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) for the character.

  * Character-related components, such as the **Character Controller** A simple, capsule-shaped collider component with specialized features for behaving as a character in a game. Unlike true collider components, a Rigidbody is not needed and the momentum effects are not realistic. [More info](class-CharacterController.html)  
See in [Glossary](Glossary.html#CharacterController).

Your project should also contain another character model with a valid Avatar.

To retarget between character models, do the following:

  1. Create a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the Hierarchy that contains
Character-related components

![](../uploads/Main/MecanimRetargetingTopLevel.png)

  1. Put the model as a child of the GameObject, together with the Animator component

![](../uploads/Main/MecanimRetargetingModel.png)

  1. Make sure scripts referencing the Animator are looking for the animator in the children instead of the root. To do this, use `GetComponentInChildren<Animator>()` instead of `GetComponent<Animator>()`.

![](../uploads/Main/MecanimRetargetingKyle.jpg)

Then in order to reuse the same animations on another model, you need to:

  1. Disable the original model
  2. Drop in the desired model as another child of GameObject

![](../uploads/Main/MecanimRetargetingOtherModel.png)

  1. Make sure the Animator Controller property for the new model is referencing the same controller asset

![](../uploads/Main/MecanimRetargetingOtherModelCorrectController.png)

  1. Tweak the character controller, the transform, and other properties on the top-level GameObject to make sure that the animations work smoothly with the new model.

![](../uploads/Main/MecanimRetargetingTed.jpg)

[](AvatarCreationandSetup.html)

Humanoid Avatar

[](InverseKinematics.html)

Inverse Kinematics

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

