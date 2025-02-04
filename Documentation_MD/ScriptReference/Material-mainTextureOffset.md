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

#  [Material](Material.html).mainTextureOffset

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

public [Vector2](Vector2.html) mainTextureOffset;

### Description

The offset of the main texture.

By default, Unity considers a texture with the property name name `"_MainTex"`
to be the main texture. Use the `[MainTexture]` [ShaderLab Properties
attribute](../Manual/SL-Properties.html) to make Unity consider a texture with
a different property name to be the main texture.  
  
This is the same as calling
[Material.GetTextureOffset](Material.GetTextureOffset.html) or
[Material.SetTextureOffset](Material.SetTextureOffset.html) with the property
name of the main texture as a parameter.  
  
Additional resources: [SetTextureOffset](Material.SetTextureOffset.html),
[GetTextureOffset](Material.GetTextureOffset.html), [ShaderLab:
Properties](../Manual/SL-Properties.html),
[ShaderPropertyFlags.MainTexture](Rendering.ShaderPropertyFlags.MainTexture.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Scroll the main texture based on time  
      
        float scrollSpeed = 0.5f;
        [Renderer](Renderer.html) rend;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)> ();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float offset = [Time.time](Time-time.html) * scrollSpeed;
            rend.material.mainTextureOffset = new [Vector2](Vector2.html)(offset, 0);
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

