[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Animation](Animation.html).Play

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-Animation.html "Go to Animation Component
in the Manual")

## Declaration

public bool Play([PlayMode](PlayMode.html) mode = PlayMode.StopSameLayer);

## Declaration

public bool Play(string animation, [PlayMode](PlayMode.html) mode =
PlayMode.StopSameLayer);

### Returns

**bool** If no name is supplied and there is no default animation, then this
method returns `false`. Otherwise, it returns `true`.

### Description

Plays an animation without blending.

If no name is supplied then the default animation plays. Use the optional
[PlayMode](PlayMode.html) to choose how this animation affects animations
already playing.  
  
If the specified animation is already playing then other animations will be
stopped but the animation will not rewind to the beginning. When the end of
the animation is reached it will automatically be stopped and rewound to the
start unless the [PlayMode](PlayMode.html) is set to Loop. If
[Animation.Play](Animation.Play.html) is called on an object during a frame
update where the object is also
[deactivated](../Manual/DeactivatingGameObjects.html) then the call will
effectively be cancelled. The animation will not start playing when the object
is later reactivated. However, if a call on a subsequent frame (while the
object is still inactive) then the animation will start playing after
reactivation.  
  
To use [Animation.Play](Animation.Play.html) the animation data must be
visible in the Inspector window. This window contains all animations for a
[GameObject](GameObject.html) in an array. As an example two animations `jump`
and `spin` are stored in the Animations list.
[Animation.Play](Animation.Play.html) can play each of these animations.
[Animation](Animation.html) can also combine animations. An (unsupported and
undocumented) [AnimationState](AnimationState.html).`layer` is used for this.
For example leaving `jump` at layer zero and moving `spin` to layer 123 will
allow them to be played together.  
  
Animations must be marked as ‘Legacy’ in the Inspector for the animations to
be found by this method. This option appears after switching the Inspector
Window to ‘Debug’.

    
    
    using UnityEngine;  
      
    // [Animation.Play](Animation.Play.html) example. Let the S and J keys start
    // a spin or jump animation. Let [Space](Space.html) play back spin and
    // jump at the same time. Let Z play spin and jump with
    // spin doubled in speed.
    //
    // Spin: rotate the cube 360 degrees in half or one second
    // Jump: bounce up to 2 units and down in one second
    //
    // Note: AnimationState.layer is no longer supported, but still exists.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Animation](Animation.html) anim;  
      
        void Start()
        {
            anim = gameObject.GetComponent<[Animation](Animation.html)>();
            anim["spin"].layer = 123;
        }  
      
        // double the spin speed when true
        private bool fastSpin = false;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // leave spin or jump to complete before changing
            if (anim.isPlaying)
            {
                return;
            }  
      
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.S](KeyCode.S.html)))
            {
                [Debug.Log](Debug.Log.html)("Spinning");
                anim.Play("spin");
            }  
      
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.J](KeyCode.J.html)))
            {
                [Debug.Log](Debug.Log.html)("Jumping");
                anim.Play("jump");
            }  
      
            // combine jump and spin
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                [Debug.Log](Debug.Log.html)("Jumping and spinning");
                anim.Play("jump");
                anim.Play("spin");
            }  
      
            // have spin speed reverted to 1.0 second
            if (fastSpin == true)
            {
                anim["spin"].speed = 1.0f;
                fastSpin = false;
            }  
      
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Z](KeyCode.Z.html)))
            {
                [Debug.Log](Debug.Log.html)("Jumping and spinning in half a second");
                anim.Play("jump");
                anim["spin"].speed = 2.0f;
                anim.Play("spin");  
      
                // we've used spin at a speed of two, now mark
                // the spin speed to revert back to one
                fastSpin = true;
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

