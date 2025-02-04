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

#  [RenderTexture](RenderTexture.html).active

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

[Switch to Manual](../Manual/class-RenderTexture.html "Go to RenderTexture
Component in the Manual")

public static [RenderTexture](RenderTexture.html) active;

### Description

Currently active render texture.

All rendering goes into the active RenderTexture. If the active RenderTexture
is `null` everything is rendered in the main window.  
  
Setting [RenderTexture.active](RenderTexture-active.html) is the same as
calling [Graphics.SetRenderTarget](Graphics.SetRenderTarget.html). Typically
you change or query the active render texture when implementing custom
graphics effects; if all you need is to make a Camera render into a texture
then use [Camera.targetTexture](Camera-targetTexture.html) instead.  
  
When a RenderTexture becomes active its hardware rendering context is
automatically created if it hasn't been created already.  
  
Additional resources:
[Graphics.SetRenderTarget](Graphics.SetRenderTarget.html),
[GraphicsTexture.active](Rendering.GraphicsTexture-active.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Get the contents of a [RenderTexture](RenderTexture.html) into a [Texture2D](Texture2D.html)
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        static public [Texture2D](Texture2D.html) GetRTPixels([RenderTexture](RenderTexture.html) rt)
        {
            // Remember currently active render texture
            [RenderTexture](RenderTexture.html) currentActiveRT = [RenderTexture.active](RenderTexture-active.html);  
      
            // Set the supplied [RenderTexture](RenderTexture.html) as the active one
            [RenderTexture.active](RenderTexture-active.html) = rt;  
      
            // Create a new [Texture2D](Texture2D.html) and read the [RenderTexture](RenderTexture.html) image into it
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(rt.width, rt.height);
            tex.ReadPixels(new [Rect](Rect.html)(0, 0, tex.width, tex.height), 0, 0);
            tex.Apply();  
      
            // Restore previously active render texture
            [RenderTexture.active](RenderTexture-active.html) = currentActiveRT;
            return tex;
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

