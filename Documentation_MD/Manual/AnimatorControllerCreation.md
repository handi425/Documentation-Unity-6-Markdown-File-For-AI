[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimatorControllerCreation.html)
  * [中文](/cn/current/Manual/AnimatorControllerCreation.html)
  * [日本語](/ja/current/Manual/AnimatorControllerCreation.html)
  * [한국어](/kr/current/Manual/AnimatorControllerCreation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimatorControllerCreation.html)
  * [中文](/cn/current/Manual/AnimatorControllerCreation.html)
  * [日本語](/ja/current/Manual/AnimatorControllerCreation.html)
  * [한국어](/kr/current/Manual/AnimatorControllerCreation.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * Create an Animator Controller

[](class-AnimatorController.html)

Animator Controller

[](Animator.html)

Animator Controller Asset

# Create an Animator Controller

You can view and set up character behavior from the **Animator Controller**
Controls animation through Animation Layers with Animation State Machines and
Animation Blend Trees, controlled by Animation Parameters. The same Animator
Controller can be referenced by multiple models with Animator components.
[More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) view (Menu: **Window** >
**Animation** > **Animator**).

To create an Animator Controller, do one of the following:

  * Select **Create** > **Animator Controller** from the Project window.
  * Right-click in the Project window and select **Create** > **Animator Controller**.
  * From the Assets menu, select **Assets** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) > **Create** > **Animator Controller**.

This creates a `.controller` asset. In the **Project Browser** window.

After the **state machine** The set of states in an Animator Controller that a
character or animated GameObject can be in, along with a set of transitions
between those states and a variable to remember the current state. The states
available will depend on the type of gameplay, but typical states include
things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) setup has been made, you can
drop the controller onto the **Animator component** A component on a model
that animates that model using the Animation system. The component has a
reference to an Animator Controller asset that controls the animation. [More
info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent) of any character with an
**Avatar** An interface for retargeting animation from one rig to another.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) in the **Hierarchy View**.

[](class-AnimatorController.html)

Animator Controller

[](Animator.html)

Animator Controller Asset

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

