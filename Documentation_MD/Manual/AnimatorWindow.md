[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimatorWindow.html)
  * [中文](/cn/current/Manual/AnimatorWindow.html)
  * [日本語](/ja/current/Manual/AnimatorWindow.html)
  * [한국어](/kr/current/Manual/AnimatorWindow.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimatorWindow.html)
  * [中文](/cn/current/Manual/AnimatorWindow.html)
  * [日本語](/ja/current/Manual/AnimatorWindow.html)
  * [한국어](/kr/current/Manual/AnimatorWindow.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * Animator Window

[](Animator.html)

Animator Controller Asset

[](AnimationStateMachines.html)

Animation State Machine

# Animator Window

Use the **Animator Window** to create, view, and modify Animator Controller
assets.

![The Animator Controller
Window](../uploads/Main/MecanimAnimatorControllerWindow.png) The Animator
Controller Window

The Animator Controller window always displays the **state machine** The set
of states in an Animator Controller that a character or animated GameObject
can be in, along with a set of transitions between those states and a variable
to remember the current state. The states available will depend on the type of
gameplay, but typical states include things like idling, walking, running and
jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) from the most recently selected
`.controller` asset, regardless of which **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) is loaded.

The Animator Controller window contains:

  * [Animation Layers](AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](AnimationLayers.html)  
See in [Glossary](Glossary.html#AnimationLayer)

  * [Event Parameters](AnimationParameters.html)
  * A layout area where you create, arrange, and connect states for your [Animator Controller](Animator.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController).

You can right-click on the grid to create a new state node. Use the middle
mouse button or press **Alt** (macOS: **Option**) and drag to pan the layout
area. Click to select and edit a state node. Click and drag a state node to
rearrange your state machine.

![The Parameters view with two parameters
created](../uploads/Main/AnimatorWindowParametersPane.png) The Parameters view
with two parameters created

Use the Parameters view to create, view, and edit [Animator Controller
Parameters](AnimationParameters.html). These are variables you define that act
as inputs for the state machine. To add a parameter, click the Plus icon and
select the parameter type from the context menu. To delete a parameter, select
the parameter in the list and press **Delete** (macOS: **Ctrl+Delete**).

![The Layers view](../uploads/Main/AnimatorWindowLayersPane.png) The Layers
view

Use the Layers view to create, view, and edit
[layers](AnimationLayers.html)Layers in Unity can be used to selectively opt
groups of GameObjects in or out of certain processes or calculations. This
includes camera rendering, lighting, physics collisions, or custom
calculations in your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#Layer) for your Animator Controller. You can
control each layer with a different state machine. For example, you can have a
base layer that controls the overall animation of your character and a second
layer that controls the upper-body animation of your character.

![The Eye icon](../uploads/Main/AnimatorWindowEyeIcon.png) The Eye icon

Enable or disable the Eye icon to display or hide the Parameters and Layers
side pane. Hide the side pane to have more room to edit your state machine.

![The breadcrumb list](../uploads/Main/AnimatorWindowBreadcrumbLocation.png)
The breadcrumb list

States can contain [sub-states](NestedStateMachines.html) and [blend
trees](class-BlendTree.html). You can nest these structures repeatedly. When
you are viewing a sub-state or blend tree within another state, the breadcrumb
list displays the nested hierarchy. Select an item in the breadcrumb list to
display the state, sub-state, or blend tree.

![The lock icon](../uploads/Main/AnimatorWindowLockIcon.png) The lock icon

Enable the lock icon to focus the Animator Window on the current state
machine. When the lock icon is enabled, the Animator window shows the same
state machine regardless of whether a different animator asset or
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) is selected. When the lock icon is
disabled and you select a different animator asset or another Game Object with
an **animator component** A component on a model that animates that model
using the Animation system. The component has a reference to an Animator
Controller asset that controls the animation. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent), the Animator Window
displays the state machine for newly selected asset or GameObject.

[](Animator.html)

Animator Controller Asset

[](AnimationStateMachines.html)

Animation State Machine

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

