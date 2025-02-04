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

#  [Camera](Camera.html).Render

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public void Render();

### Description

Render the camera manually.

This will render the camera. It will use the camera's clear flags, target
texture and all other settings.  
  
The camera will send [OnPreCull](MonoBehaviour.OnPreCull.html),
[OnPreRender](MonoBehaviour.OnPreRender.html) and
[OnPostRender](MonoBehaviour.OnPostRender.html) to any scripts attached, and
render any eventual image filters.  
  
This is used for taking precise control of render order. To make use of this
feature, create a camera and disable it. Then call Render on it.  
  
You are not able to call the Render function from a camera that is currently
rendering. If you wish to do this create a copy of the camera, and make it
match the original one using [CopyFrom](Camera.CopyFrom.html).  
  
Additional resources: [RenderWithShader](Camera.RenderWithShader.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Take a "screenshot" of a camera's Render [Texture](Texture.html).
        [Texture2D](Texture2D.html) RTImage([Camera](Camera.html) camera)
        {
            // The Render [Texture](Texture.html) in [RenderTexture.active](RenderTexture-active.html) is the one
            // that will be read by ReadPixels.
            var currentRT = [RenderTexture.active](RenderTexture-active.html);
            [RenderTexture.active](RenderTexture-active.html) = camera.targetTexture;  
      
            // Render the camera's view.
            camera.Render();  
      
            // Make a new texture and read the active Render [Texture](Texture.html) into it.
            [Texture2D](Texture2D.html) image = new [Texture2D](Texture2D.html)(camera.targetTexture.width, camera.targetTexture.height);
            image.ReadPixels(new [Rect](Rect.html)(0, 0, camera.targetTexture.width, camera.targetTexture.height), 0, 0);
            image.Apply();  
      
            // Replace the original active Render [Texture](Texture.html).
            [RenderTexture.active](RenderTexture-active.html) = currentRT;
            return image;
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

