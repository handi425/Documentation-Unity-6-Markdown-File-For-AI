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

# AnimationEvent

class in UnityEngine

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

[ ]()

### Description

AnimationEvent lets you call a script function similar to SendMessage as part
of playing back an animation.

Animation events support functions that take zero or one parameter. The
parameter can be a float, an int, a string, an object reference, or an
AnimationEvent.

    
    
    // [Animation](Animation.html) [Event](Event.html) example
    // Small example that can be called on each specified frame.
    // The code is executed once per animation loop.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public void PrintEvent()
        {
            [Debug.Log](Debug.Log.html)("PrintEvent");
        }
    }
    

A more detailed example below shows a more complex way of creating an
animation. In this script example the `Animator` component is accessed and a
`Clip` from it obtained. (This clip was set up in the Animation window.) The
clip lasts for 2 seconds. An `AnimationEvent` is created, and has parameters
set. The parameters include the function `PrintEvent()` which will handle the
event. The event is then added to the clip. This all happens in `Start()`.
Once the game has launched the event is called after 1.3s and then repeats
every 2s.

    
    
    // Add an [Animation](Animation.html) [Event](Event.html) to a [GameObject](GameObject.html) that has an [Animator](Animator.html)
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public void Start()
        {
            // existing components on the [GameObject](GameObject.html)
            [AnimationClip](AnimationClip.html) clip;
            [Animator](Animator.html) anim;  
      
            // new event created
            [AnimationEvent](AnimationEvent.html) evt;
            evt = new [AnimationEvent](AnimationEvent.html)();  
      
            // put some parameters on the [AnimationEvent](AnimationEvent.html)
            //  - call the function called PrintEvent()
            //  - the animation on this object lasts 2 seconds
            //    and the new animation created here is
            //    set up to happen 1.3s into the animation
            evt.intParameter = 12345;
            evt.time = 1.3f;
            evt.functionName = "PrintEvent";  
      
            // get the animation clip and add the [AnimationEvent](AnimationEvent.html)
            anim = GetComponent<[Animator](Animator.html)>();
            clip = anim.runtimeAnimatorController.animationClips[0];
            clip.AddEvent(evt);
        }  
      
        // the function to be called as an event
        public void PrintEvent(int i)
        {
            print("PrintEvent: " + i + " called at: " + [Time.time](Time-time.html));
        }
    }
    

### Properties

[animationState](AnimationEvent-animationState.html)| The animation state that
fired this event (Read Only).  
---|---  
[animatorClipInfo](AnimationEvent-animatorClipInfo.html)| The animator clip
info related to this event (Read Only).  
[animatorStateInfo](AnimationEvent-animatorStateInfo.html)| The animator state
info related to this event (Read Only).  
[floatParameter](AnimationEvent-floatParameter.html)| Float parameter that is
stored in the event and will be sent to the function.  
[functionName](AnimationEvent-functionName.html)| The name of the function
that will be called.  
[intParameter](AnimationEvent-intParameter.html)| Int parameter that is stored
in the event and will be sent to the function.  
[isFiredByAnimator](AnimationEvent-isFiredByAnimator.html)| Returns true if
this Animation event has been fired by an Animator component.  
[isFiredByLegacy](AnimationEvent-isFiredByLegacy.html)| Returns true if this
Animation event has been fired by an Animation component.  
[messageOptions](AnimationEvent-messageOptions.html)| Function call options.  
[objectReferenceParameter](AnimationEvent-objectReferenceParameter.html)|
Object reference parameter that is stored in the event and will be sent to the
function.  
[stringParameter](AnimationEvent-stringParameter.html)| String parameter that
is stored in the event and will be sent to the function.  
[time](AnimationEvent-time.html)| The time at which the event will be fired
off.  
  
### Constructors

[AnimationEvent](AnimationEvent-ctor.html)| Creates a new animation event.  
---|---  
  
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

