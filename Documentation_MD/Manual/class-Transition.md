[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Transition.html)
  * [中文](/cn/current/Manual/class-Transition.html)
  * [日本語](/ja/current/Manual/class-Transition.html)
  * [한국어](/kr/current/Manual/class-Transition.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Transition.html)
  * [中文](/cn/current/Manual/class-Transition.html)
  * [日本語](/ja/current/Manual/class-Transition.html)
  * [한국어](/kr/current/Manual/class-Transition.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * Animation transitions

[](StateMachineTransitions.html)

State Machine Transitions

[](class-BlendTree.html)

Animation Blend Trees

# Animation transitions

Use **animation transitions** Allows a state machine to switch or blend from
one animation state to another. Transitions define how long a blend between
states should take, and the conditions that activate them. [More
info](StateMachineTransitions.html)  
See in [Glossary](Glossary.html#AnimationTransition) in the [state
machine](StateMachineBasics.html)The set of states in an Animator Controller
that a character or animated GameObject can be in, along with a set of
transitions between those states and a variable to remember the current state.
The states available will depend on the type of gameplay, but typical states
include things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) to switch or blend from one
animation state to another. Transitions define the duration of the blend
between states and the conditions when a transition occurs. To set these
conditions, specify values of parameters in the **Animator Controller**
Controls animation through Animation Layers with Animation State Machines and
Animation Blend Trees, controlled by Animation Parameters. The same Animator
Controller can be referenced by multiple models with Animator components.
[More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController).

For example, your character might have a “patrolling” state and a “sleeping”
state. You can set the transition between patrolling and sleeping to occur
only when an “alertness” parameter value decreases below a certain level.

![An example of a transition as viewed in the
inspector.](../uploads/Main/classTransitionAnimatorPreview.jpg) An example of
a transition as viewed in the inspector.

To name a transition, type its name in the following the field:

![](../uploads/Main/AnimatorTransitionName.png)

The **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window displays the transitions
that the state uses:

![](../uploads/Main/AnimatorTransitionNameInState.png)

You can only activate one transition at a given time. However, you can
configure the settings to interrupt the currently active transition with
another transition. Refer to Transition interruption for more information.

## Transition properties

To view the properties for a transition, select the transition line connecting
two states in the **Animator window** The window where the Animator Controller
is visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow). The properties appear in the
Inspector window.

![](../uploads/Main/class-Transition-Properties.png)

Use the following properties to adjust the transition and how it blends
between the current and next state.

**Property** | **Function**  
---|---  
**Has Exit Time** |  **Exit Time** is a special transition that doesn’t rely on a parameter. Instead, it relies on the normalized time of the state. Check to make the transition happen at the specific time specified in **Exit Time**.  
**Settings** | Fold-out menu containing detailed transition settings. Each transition setting is described below.  
**Exit Time** | If **Has Exit Time** is checked, this value represents the exact time at which the transition can take effect. This is represented in normalized time (for example, an exit time of 0.75 means that on the first frame where 75% of the animation has played, the **Exit Time** condition is true). On the next frame, the condition is false.  
  
For looped animations, transitions with exit times smaller than 1 are
evaluated every loop, so you can use this to time your transition with the
proper timing in the animation every loop.  
  
Transitions with an **Exit Time** greater than 1 are evaluated only once, so
they can be used to exit at a specific time after a fixed number of loops. For
example, a transition with an exit time of 3.5 are evaluated once, after three
and a half loops.  
**Fixed Duration** | If the **Fixed Duration** box is checked, the transition time is interpreted in seconds. If the **Fixed Duration** box is not checked, the transition time is interpreted as a fraction of the normalized time of the source state.  
**Transition Duration** | The duration of the transition, in normalized time or seconds depending on the **Fixed Duration** mode, relative to the current state’s duration. This is visualized in the transition graph as the portion between the two blue markers.  
**Transition Offset** | The offset of the time to begin playing in the destination state which is transitioned to. For example, a value of 0.5 means the target state begins playing at 50% of the way through its own timeline.  
**Interruption Source** | Use this to control the circumstances under which this transition might be interrupted. For more information, refer to Transition interruption.  
**Ordered Interruption** | Determines whether the current transition can be interrupted by other transitions independently of their order (see Transition interruption below).  
**Conditions** | A transition can have a single condition, multiple conditions, or no conditions at all. If your transition has no conditions, the Unity Editor only considers the **Exit Time** , and the transition occurs when the exit time is reached. If your transition has one or more conditions, the conditions must all be met before the transition is triggered.  
  
A condition consists of:  
  
\- An event parameter (the value considered in the condition).  
\- A conditional predicate (if needed,for example, ‘less than’ or ‘greater
than’ for floats).  
\- A parameter value (if needed).  
  
If you have **Has Exit Time** selected for the transition and have one or more
conditions, note that the Unity Editor considers whether the conditions are
true after the **Exit Time**. This allows you to ensure that your transition
occurs during a certain portion of the animation.  
  
## Transition interruption

Use the **Interruption Source** and **Ordered Interruption** properties to
control how your transition can be interrupted.

The interruption order works, conceptually, as if transitions are queued and
then parsed for a valid transition from the first transition inserted to the
last.

### Interruption Source property

The transitions in [AnyState](class-State.html) are always added first in the
queue, then other transitions are queued depending on the value of
**Interruption Source** :

**Value** | **Function**  
---|---  
**None** | Don’t add any more transitions.  
**Current State** | Queue the transitions from the current state.  
**Next State** | Queue the transitions from the next state.  
**Current State then Next State** | Queue the transitions from the current state, then queue the ones from the next state.  
**Next State then Current State** | Queue the transitions from the next state, then queue the ones from the current state.  
  
### Ordered Interruption property

The property **Ordered Interruption** changes how the queue is parsed.

Depending on its value, parsing the queue ends at a different moment as listed
below.

**Value** | **Ends when**  
---|---  
**Checked** | A valid transition or the current transition has been found.  
**Unchecked** | A valid transition has been found.  
  
Only an [AnyState](class-State.html) transition can be interrupted by itself.
To learn more about transition interruptions, refer to [State Machine
Transition Interruptions](https://unity.com/blog/engine-platform/state-
machine-transition-interruptions).

## Transition graph

Use the Transition graph to visually adjust the transition settings.

![The Transition graph as shown in the
Inspector.](../uploads/Main/AnimatorTransitionSettingsAndGraph.svg) The
Transition graph as shown in the Inspector.

The white line in the Transition graph represents IK foot contact for each
State. The top of the graph represents the Left foot and the bottom represents
the Right foot. When the white line is at the top of the graph, the Left foot
contacts the floor plane. When the white line is at the bottom, the Right foot
contacts the floor plane.

Adjust the transition settings until there is a smooth transition between
states. A white line with a smooth transition avoids foot slips, jumps in
animation, and preserves the dynamics of the motion.

Use the following manipulations to adjust the transition settings:

  * Drag the **Duration “out”** marker to change the **Duration** of the transition.
  * Drag the **Duration “in”** marker to change the duration of the transition and the **Exit Time**.
  * Drag the target state to adjust the **Transition Offset**.
  * Drag the preview playback marker to scrub through the animation blend in the preview window at the bottom of the Inspector.

## Transitions between Blend Tree states

If either the current or next state belonging to this transition is a [Blend
Tree](class-BlendTree.html) state, the Blend Tree parameters appear in the
**Inspector** window. Adjust these values to preview how your transition looks
with the Blend Tree values set to different configurations. If your Blend Tree
contains clips of differing lengths, you should test what your transition
looks like when showing both the short clip and the long clip. Adjusting these
values does not affect how the transition behaves at runtime; they are solely
for helping you preview how the transition could look in different situations.

![The Blend Tree parameter preview controls, visible when either your current
or next state is a Blend Tree
state.](../uploads/Main/AnimatorTransitionInspectorShowingBlendtreeParams.png)
The Blend Tree parameter preview controls, visible when either your current or
next state is a Blend Tree state.

## Conditions

A transition can have a single condition, multiple conditions, or no
conditions. If your transition has no conditions, the Unity Editor only
considers the **Exit Time** , and the transition occurs when the exit time is
reached. If your transition has one or more conditions, the conditions must
all be met before the transition is triggered.

A condition consists of:

  * An event parameter, the value of which is considered in the condition.
  * A conditional predicate, if needed (for example, less or greater for floats).
  * A parameter value, if needed.

If you enabled **Has Exit Time** for the transition and the transition has one
or more conditions, Unity only checks these conditions after the exit time of
the state. This ensures that your transition only occurs during a certain
portion of the animation.

Transition

[](StateMachineTransitions.html)

State Machine Transitions

[](class-BlendTree.html)

Animation Blend Trees

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

