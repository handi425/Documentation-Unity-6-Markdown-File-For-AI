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

#  [Texture2D](Texture2D.html).ReadPixels

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

public void ReadPixels([Rect](Rect.html) source, int destX, int destY, bool
recalculateMipMaps = true);

### Parameters

source | The region of the render target to read from.  
---|---  
destX | The x position in the texture to write the pixels to.  
destY | The y position in the texture to write the pixels to.  
recalculateMipMaps | When the value is `true`, Unity automatically recalculates the mipmap for the texture after it writes the pixel data. Otherwise, Unity doesn't do this automatically.  
  
### Description

Reads pixels from the current render target and writes them to a texture.

This method copies a rectangular area of pixel colors from the currently
active render target on the GPU (for example the screen, a
[RenderTexture](RenderTexture.html), or a
[GraphicsTexture](Rendering.GraphicsTexture.html)) and writes them to a
texture on the CPU at position (`destX`, `destY`).
[Texture.isReadable](Texture-isReadable.html) must be `true`, and you must
call [Apply](Texture2D.Apply.html) after `ReadPixels` to upload the changed
pixels to the GPU.  
  
The lower left corner is (0, 0).  
  
`ReadPixels` is usually slow, because the method waits for the GPU to complete
all previous work first. To copy a texture more quickly, use one of the
following methods instead:

  * [AsyncGPUReadback.RequestIntoNativeArray](Rendering.AsyncGPUReadback.RequestIntoNativeArray.html) to copy a texture from the GPU to the CPU.
  * [Graphics.CopyTexture](Graphics.CopyTexture.html), [CommandBuffer.CopyTexture](Rendering.CommandBuffer.CopyTexture.html) or [Graphics.Blit](Graphics.Blit.html) to copy a texture on the GPU only.

The render target and the texture must use the same format, and the format
must be supported on the device for both rendering and sampling.  
  
You can automatically update the mipmap when you call
[Apply](Texture2D.Apply.html) instead of setting `recalculateMipMaps` to
`true`.  
  
The following code example demonstrates how to use `ReadPixels` in the Built-
in Render Pipeline. In Scriptable Render Pipelines such as the Universal
Render Pipeline (URP), [Camera.onPostRender](Camera-onPostRender.html) isn't
available, but you can use
[RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-
endCameraRendering.html) in a similar way.

    
    
    using UnityEngine;  
      
    public class ReadPixelsExample : [MonoBehaviour](MonoBehaviour.html)
    {
        // Set [Renderer](Renderer.html) to a [GameObject](GameObject.html) that has a [Renderer](Renderer.html) component and a material that displays a texture
        public [Renderer](Renderer.html) screenGrabRenderer;  
      
        private [Texture2D](Texture2D.html) destinationTexture;
        private bool isPerformingScreenGrab;  
      
        void Start()
        {
            // Create a new [Texture2D](Texture2D.html) with the width and height of the screen, and cache it for reuse
            destinationTexture = new [Texture2D](Texture2D.html)([Screen.width](Screen-width.html), [Screen.height](Screen-height.html), [TextureFormat.RGB24](TextureFormat.RGB24.html), false);  
      
            // Make screenGrabRenderer display the texture.
            screenGrabRenderer.material.mainTexture = destinationTexture;  
      
            // Add the onPostRender callback
            [Camera.onPostRender](Camera-onPostRender.html) += OnPostRenderCallback;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // When the user presses the [Space](Space.html) key, perform the screen grab operation
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                isPerformingScreenGrab = true;
            }
        }  
      
        void OnPostRenderCallback([Camera](Camera.html) cam)
        {
            if (isPerformingScreenGrab)
            {
                // Check whether the [Camera](Camera.html) that just finished rendering is the one you want to take a screen grab from
                if (cam == [Camera.main](Camera-main.html))
                {
                    // Define the parameters for the ReadPixels operation
                    [Rect](Rect.html) regionToReadFrom = new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html));
                    int xPosToWriteTo = 0;
                    int yPosToWriteTo = 0;
                    bool updateMipMapsAutomatically = false;  
      
                    // Copy the pixels from the [Camera](Camera.html)'s render target to the texture
                    destinationTexture.ReadPixels(regionToReadFrom, xPosToWriteTo, yPosToWriteTo, updateMipMapsAutomatically);  
      
                    // Upload texture data to the GPU, so the GPU renders the updated texture
                    // Note: This method is costly, and you should call it only when you need to
                    // If you do not intend to render the updated texture, there is no need to call this method at this point
                    destinationTexture.Apply();  
      
                    // Reset the isPerformingScreenGrab state
                    isPerformingScreenGrab = false;
                }
            }
        }  
      
        // Remove the onPostRender callback
        void OnDestroy()
        {
            [Camera.onPostRender](Camera-onPostRender.html) -= OnPostRenderCallback;
        }
    }
    

Additional resources:
[ImageConversion.EncodeToPNG](ImageConversion.EncodeToPNG.html).

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

