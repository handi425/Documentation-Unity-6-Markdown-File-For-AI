[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ScriptingRootMotion.html)
  * [中文](/cn/current/Manual/ScriptingRootMotion.html)
  * [日本語](/ja/current/Manual/ScriptingRootMotion.html)
  * [한국어](/kr/current/Manual/ScriptingRootMotion.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ScriptingRootMotion.html)
  * [中文](/cn/current/Manual/ScriptingRootMotion.html)
  * [日本語](/ja/current/Manual/ScriptingRootMotion.html)
  * [한국어](/kr/current/Manual/ScriptingRootMotion.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Humanoid Avatar](AvatarCreationandSetup.html)
  * Scripting Root Motion

[](RootMotion.html)

How Root Motion works

[](class-Animator.html)

Animator component

# Scripting Root Motion

Sometimes your animation comes as “in-place”, which means if you put it in a
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), it will not move the character that
it’s on. In other words, the animation does not contain “**root motion**
Motion of character’s root node, whether it’s controlled by the animation
itself or externally. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootMotion)”. For this, we can modify root
motion from script. To put everything together follow the steps below (note
there are many variations of achieving the same result, this is just one
recipe).

  * Open the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) for the FBX file that contains the
in-place animation, and go to the **Animation** tab

  * Make sure the **Muscle Definition** This allows you to have more intuitive control over the character’s skeleton. When an Avatar is in place, the Animation system works in muscle space, which is more intuitive than bone space. [More info](MuscleDefinitions.html)  
See in [Glossary](Glossary.html#Muscledefinition) is set to the **Avatar** An
interface for retargeting animation from one rig to another. [More
info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) you intend to control (let’s say this
avatar is called _Dude_ , and it has already been added to the **Hierarchy
View**).

  * Select the **animation clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) from the available clips

  * Make sure **Loop Pose** An animation clip setting that blends the end and start of an animation to create a seamless join. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#LoopPose) is properly aligned (the light next
to it is green), and that the checkbox for **Loop Pose** is clicked

![](../uploads/Main/MecanimRootMotionChristmasTree.png)

  * Preview the animation in the animation viewer to make sure the beginning and the end of the animation align smoothly, and that the character is moving “in-place”
  * On the animation clip [create a curve](animeditor-AnimationCurves.html) that will control the speed of the character (you can add a curve from the **Animation Import inspector** **Curves- > +**)
  * Name that curve something meaningful, like “Runspeed”

![](../uploads/Main/MecanimRootMotionCurve.png)

  * Create a new **Animator Controller** Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), (let’s call it
**RootMotionController**)

  * Drop the desired animation clip into it, this should create a state with the name of the animation (say **Run**)
  * Add a parameter to the Controller with the same name as the curve (in this case, “Runspeed”)

![](../uploads/Main/MecanimRootMotionController.png)

  * Select the character **Dude** in the **Hierarchy** , whose inspector should already have an **Animator** component.
  * Drag **RootMotionController** onto the **Controller** property of the Animator
  * If you press play now, you should see the “Dude” running in place

Finally, to control the motion, we will need to create a script
(RootMotionScript.cs), that implements the
[OnAnimatorMove](../ScriptReference/MonoBehaviour.OnAnimatorMove.html)
callback:-

    
    
    using UnityEngine;
    using System.Collections;
    
    [RequireComponent(typeof(Animator))]
    
    public class RootMotionScript : MonoBehaviour {
    
        void OnAnimatorMove()
        {
                Animator animator = GetComponent<Animator>();
    
                if (animator)
                {
         Vector3 newPosition = transform.position;
                   newPosition.z += animator.GetFloat("Runspeed") * Time.deltaTime;
         transform.position = newPosition;
                }
        }
    }
    
    

You should attach RootMotionScript.cs to the “Dude” object. When you do this,
the **Animator component** A component on a model that animates that model
using the Animation system. The component has a reference to an Animator
Controller asset that controls the animation. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent) will detect that the script
has an [OnAnimatorMove](../ScriptReference/MonoBehaviour.OnAnimatorMove.html)
function and show the **Apply Root Motion** property as _Handled by Script_

![](../uploads/Main/MecanimRootMotionDude.png)

[](RootMotion.html)

How Root Motion works

[](class-Animator.html)

Animator component

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

