[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TargetMatching.html)
  * [中文](/cn/current/Manual/TargetMatching.html)
  * [日本語](/ja/current/Manual/TargetMatching.html)
  * [한국어](/kr/current/Manual/TargetMatching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TargetMatching.html)
  * [中文](/cn/current/Manual/TargetMatching.html)
  * [日本語](/ja/current/Manual/TargetMatching.html)
  * [한국어](/kr/current/Manual/TargetMatching.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animator Controller](class-AnimatorController.html)
  * [Animation State Machine](AnimationStateMachines.html)
  * Target Matching

[](AnimationSoloMute.html)

State Machine Solo and Mute

[](AnimatorOverrideController.html)

Animator Override Controller

# Target Matching

Often in games, a situation arises where a character must move in such a way
that a hand or foot lands at a certain place at a certain time. For example,
the character may need to jump across stepping stones or jump and grab an
overhead beam.

You can use the [Animator.MatchTarget
function](../ScriptReference/Animator.MatchTarget.html) to handle this kind of
situation. Imagine, for example, you want to arrange a situation where the
character jumps onto a platform and you already have an **animation clip**
Animation data that can be used for animated characters or simple animations.
It is a simple “unit” piece of motion, such as (one specific instance of)
“Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) for it called _Jump Up_.
Firstly, you need to find the place in the animation clip at which the
character is beginning to get off the ground, note in this case it is 14.1% or
0.141 into the animation clip in normalized time:

![](../uploads/Main/MecanimMatchTargetStart.png)

You also need to find the place in the animation clip where the character is
about to land on its feet, which in this case is at 78.0% or 0.78.

![](../uploads/Main/MecanimMatchTargetEnd.png)

With this information, you can create a script that calls
[MatchTarget](../ScriptReference/Animator.MatchTarget.html) which you can
attach to the model:

    
    
    using UnityEngine;
    using System;
    
    [RequireComponent(typeof(Animator))]
    public class TargetCtrl : MonoBehaviour {
    
        protected Animator animator;
    
        //the platform object in the scene
        public Transform jumpTarget = null;
        void Start () {
            animator = GetComponent<Animator>();
        }
    
        void Update () {
            if(animator) {
                if(Input.GetButton("Fire1"))         
                    animator.MatchTarget(jumpTarget.position, jumpTarget.rotation, AvatarTarget.LeftFoot,
                                                           new MatchTargetWeightMask(Vector3.one, 1f), 0.141f, 0.78f);
            }       
        }
    }
    
    
    

The script will move the character so that it jumps from its current position
and lands with its left foot at the target. Bear in mind that the result of
using MatchTarget will generally only make sense if it is called at the right
point in gameplay.

[](AnimationSoloMute.html)

State Machine Solo and Mute

[](AnimatorOverrideController.html)

Animator Override Controller

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

