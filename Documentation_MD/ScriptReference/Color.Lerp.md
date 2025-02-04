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

#  [Color](Color.html).Lerp

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

## Declaration

public static [Color](Color.html) Lerp([Color](Color.html) a,
[Color](Color.html) b, float t);

### Parameters

a | Color a.  
---|---  
b | Color b.  
t | Float for combining a and b.  
  
### Description

Linearly interpolates between colors `a` and `b` by `t`.

`t` is clamped between 0 and 1. When `t` is 0 returns `a`. When `t` is 1
returns `b`.  
  
The code sample sets the color of a GameObject's material to a value between
white and black, based on the amount of time that has elapsed.

    
    
    using UnityEngine;  
      
    public class ColorLerp : [MonoBehaviour](MonoBehaviour.html)
    {
        [Color](Color.html) lerpedColor = [Color.white](Color-white.html);
        [Renderer](Renderer.html) renderer;  
      
        void Start()
        {
            renderer = GetComponent<[Renderer](Renderer.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            lerpedColor = [Color.Lerp](Color.Lerp.html)([Color.white](Color-white.html), [Color.black](Color-black.html), [Mathf.PingPong](Mathf.PingPong.html)([Time.time](Time-time.html), 1));
            renderer.material.color = lerpedColor;
        }
    }
    

Additional resources: [LerpUnclamped](Color.LerpUnclamped.html).

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

