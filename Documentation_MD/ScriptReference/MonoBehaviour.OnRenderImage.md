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

#
[MonoBehaviour](MonoBehaviour.html).OnRenderImage(RenderTexture,RenderTexture)

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Parameters

source | A [RenderTexture](RenderTexture.html) containing the source image.  
---|---  
destination | The [RenderTexture](RenderTexture.html) to update with the modified image.  
  
### Description

[Event function](../Manual/event-functions.html) that Unity calls after a
[Camera](Camera.html) has finished rendering, that allows you to modify the
Camera's final image.

In the Built-in Render Pipeline, Unity calls `OnRenderImage` on MonoBehaviours
that are attached to the same GameObject as an enabled [Camera](Camera.html)
component, after the Camera finished rendering. You can use `OnRenderImage` to
create a fullscreen post-processing effect. These effects work by reading the
pixels from the source image, using a Unity shader to modify the appearance of
the pixels, and then rendering the result into the destination image. You
would typically use [Graphics.Blit](Graphics.Blit.html) to perform these
steps.  
  
If multiple scripts on the same Camera implement `OnRenderImage`, Unity calls
them in the order that they appear in the Camera Inspector window, starting
from the top. The `destination` of one operation is the `source` of the next
one; internally, Unity creates one or more temporary RenderTextures to store
these intermediate results.  
  
On Android, to avoid banding or to use alpha in fullscreen effects, set
[PlayerSettings.use32BitDisplayBuffer](PlayerSettings-
use32BitDisplayBuffer.html) to `true`.  
  
`OnRenderImage` is not supported in the Scriptable Render Pipeline. To create
custom fullscreen effects in the Universal Render Pipeline (URP), use the
[ScriptableRenderPass](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRenderPass.html)
API. To create custom fullscreen effects in the High Definition Render
Pipeline (HDRP), use a [Fullscreen Custom
Pass](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-
definition@latest/index.html?subfolder=/manual/Custom-Pass.html).  
  
For information about using Unity's pre-built post-processing effects, see
[Post-processing](../Manual/PostProcessingOverview.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // A [Material](Material.html) with the Unity shader you want to process the image with
        public [Material](Material.html) mat;  
      
        void OnRenderImage([RenderTexture](RenderTexture.html) src, [RenderTexture](RenderTexture.html) dest)
        {
            // Read pixels from the source [RenderTexture](RenderTexture.html), apply the material, copy the updated results to the destination [RenderTexture](RenderTexture.html)
            [Graphics.Blit](Graphics.Blit.html)(src, dest, mat);
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

