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

#  [Animator](Animator.html).Play

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

[Switch to Manual](../Manual/class-Animator.html "Go to Animator Component in
the Manual")

## Declaration

public void Play(string stateName, int layer = -1, float normalizedTime =
float.NegativeInfinity);

## Declaration

public void Play(int stateNameHash, int layer = -1, float normalizedTime =
float.NegativeInfinity);

### Parameters

stateName | The state name.  
---|---  
stateNameHash | The state hash name. If stateNameHash is 0, it changes the current state time.  
layer | The layer index. If layer is -1, it plays the first state with the given state name or hash.  
normalizedTime | The time offset between zero and one.  
  
### Description

Plays a state.

When you specify a state name, or the string used to generate a hash, it
should include the name of the parent layer. For example, if you have a
`Bounce` state in the `Base Layer`, the name is `Base Layer.Bounce`. The
`normalizedTime` parameter varies between 0 and 1. If this parameter is left
at zero then [Play](Animator.Play.html) will operate as expected. A different
starting point can be given. An example could be `normalizedTime` set to 0.5,
which means the animation starts halfway through. If the transition from one
state switches to another, it may or may not be blended. If the transition
starts at 0.75 it will be blended with the other state. If no transition is
set up then [Play](Animator.Play.html) will continue to 1.0 with no changes.  
  
![](../StaticFiles/ScriptRefImages/AnimatorPlay.png)  
_The following example script animates a cube._  
  
This cube has two Animator states called `Rest` and `Bounce`. An empty
animation is played in the `Rest` state. When the Space key is pressed the
cube switches into the `Bounce` state. This causes the cube to jump up and
down twice. The cube then returns to the `Rest` state. Because `Bounce` is
selected from the [Animator.Play](Animator.Play.html) script, no Transition is
needed. However the return from `Bounce` to `Rest` does have a Transition.
`Has Exit Time` is ticked to make `Bounce` last for its one second. Attach
this script to the GameObject you want to animate.

    
    
    using UnityEngine;  
      
    // Press the space key in Play [Mode](Scripting.GarbageCollector.Mode.html) to switch to the Bounce state.  
      
    public class Move : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Animator](Animator.html) anim;  
      
        void Start()
        {
            anim = GetComponent<[Animator](Animator.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                if (anim != null)
                {
                    // play Bounce but start at a quarter of the way through
                    anim.Play("Base Layer.Bounce", 0, 0.25f);
                }
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

