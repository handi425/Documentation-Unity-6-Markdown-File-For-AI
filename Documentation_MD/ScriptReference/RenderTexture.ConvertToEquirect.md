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

#  [RenderTexture](RenderTexture.html).ConvertToEquirect

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

## Declaration

public void ConvertToEquirect([RenderTexture](RenderTexture.html) equirect,
[Camera.MonoOrStereoscopicEye](Camera.MonoOrStereoscopicEye.html) eye);

### Parameters

equirect | RenderTexture to render the equirect format to.  
---|---  
eye | A Camera eye corresponding to the left or right eye for stereoscopic rendering, or neither for monoscopic rendering.  
  
### Description

Converts the render texture to equirectangular format (both stereoscopic or
monoscopic equirect). The left eye will occupy the top half and the right eye
will occupy the bottom. The monoscopic version will occupy the whole texture.
Texture dimension must be of type
[TextureDimension.Cube](Rendering.TextureDimension.Cube.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class CreateEquirect : [MonoBehaviour](MonoBehaviour.html)
    {
        public [RenderTexture](RenderTexture.html) cubemap;
        public [RenderTexture](RenderTexture.html) cubemap2;
        public [RenderTexture](RenderTexture.html) equirect;
        public bool renderStereo = true;
        public float stereoSeparation = 0.064f;  
      
        void LateUpdate()
        {
            //assume cubemap and cubemap2 are rendered using [Camera.RenderToCubemap](Camera.RenderToCubemap.html)() for left/right eyes  
      
            if (equirect == null)
                return;  
      
            if (renderStereo)
            {
                cubemap.ConvertToEquirect(equirect, [Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html));
                cubemap2.ConvertToEquirect(equirect, [Camera.MonoOrStereoscopicEye.Right](Camera.MonoOrStereoscopicEye.Right.html));
            }
            else
            {
                cubemap.ConvertToEquirect(equirect, [Camera.MonoOrStereoscopicEye.Mono](Camera.MonoOrStereoscopicEye.Mono.html));
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

