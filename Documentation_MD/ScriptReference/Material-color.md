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

#  [Material](Material.html).color

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

[Switch to Manual](../Manual/class-Material.html "Go to Material Component in
the Manual")

public [Color](Color.html) color;

### Description

The main color of the Material.

By default, Unity considers a color with the property name name `"_Color"` to
be the main color. Use the `[MainColor]` [ShaderLab Properties
attribute](../Manual/SL-Properties.html) to make Unity consider a color with a
different property name to be the main color.  
  
This is the same as calling [GetColor](Material.GetColor.html) or
[SetColor](Material.SetColor.html) with the property name of the main color as
a parameter.  
  
Additional resources: [SetColor](Material.SetColor.html),
[GetColor](Material.GetColor.html), [ShaderLab: Properties](../Manual/SL-
Properties.html),
[ShaderPropertyFlags.MainColor](Rendering.ShaderPropertyFlags.MainColor.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Fade the color from red to green
        // back and forth over the defined duration  
      
        [Color](Color.html) colorStart = [Color.red](Color-red.html);
        [Color](Color.html) colorEnd = [Color.green](Color-green.html);
        float duration = 1.0f;
        [Renderer](Renderer.html) rend;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)> ();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float lerp = [Mathf.PingPong](Mathf.PingPong.html)([Time.time](Time-time.html), duration) / duration;
            rend.material.color = [Color.Lerp](Color.Lerp.html)(colorStart, colorEnd, lerp);
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

