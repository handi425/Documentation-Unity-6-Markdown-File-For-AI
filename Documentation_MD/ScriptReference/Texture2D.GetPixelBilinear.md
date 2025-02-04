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

#  [Texture2D](Texture2D.html).GetPixelBilinear

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

public [Color](Color.html) GetPixelBilinear(float u, float v, int mipLevel =
0);

### Parameters

u | The u coordinate of the pixel to get.  
---|---  
v | The v coordinate of the pixel to get.  
mipLevel | The mipmap level to read from. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html). The default value is `0`.  
  
### Returns

**Color** The pixel color.

### Description

Gets the filtered pixel color at the normalized coordinates (`u`, `v`).

This method gets pixel data from the texture in CPU memory.
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
Unity uses bilinear filtering to return the pixel color.  
  
The lower left corner is (0, 0). If the pixel coordinate is outside the
texture's dimensions, Unity clamps or repeats it, depending on the texture's
[TextureWrapMode](TextureWrapMode.html).  
  
You can't use `GetPixelBilinear` with textures that use Crunch texture
compression. Use [GetPixels32](Texture2D.GetPixels32.html) instead.  
  
Additional resources: [GetPixel](Texture2D.GetPixel.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // "Warp" a texture by squashing its pixels to one side.
        // This involves sampling the image at non-integer pixel
        // positions to ensure a smooth effect.  
      
        // Source image.
        public [Texture2D](Texture2D.html) sourceTex;  
      
        // Amount of "warping".
        public float warpFactor = 1.0f;  
      
        [Texture2D](Texture2D.html) destTex;
        [Color](Color.html)[] destPix;  
      
    
        void Start()
        {
            // Set up a new texture with the same dimensions as the original.
            destTex = new [Texture2D](Texture2D.html)(sourceTex.width, sourceTex.height);
            destPix = new [Color](Color.html)[destTex.width * destTex.height];  
      
            // For each pixel in the destination texture...
            for (var y = 0; y < destTex.height; y++)
            {
                for (var x = 0; x < destTex.width; x++)
                {
                    // Calculate the fraction of the way across the image
                    // that this pixel positon corresponds to.
                    float xFrac = x * 1.0f / (destTex.width - 1);
                    float yFrac = y * 1.0f / (destTex.height - 1);  
      
                    // Take the fractions (0..1)and raise them to a power to apply
                    // the distortion.
                    float warpXFrac = [Mathf.Pow](Mathf.Pow.html)(xFrac, warpFactor);
                    float warpYFrac = [Mathf.Pow](Mathf.Pow.html)(yFrac, warpFactor);  
      
                    // Get the non-integer pixel positions using GetPixelBilinear.
                    destPix[y * destTex.width + x] = sourceTex.GetPixelBilinear(warpXFrac, warpYFrac);
                }
            }  
      
            // Copy the pixel data to the destination texture and apply the change.
            destTex.SetPixels(destPix);
            destTex.Apply();  
      
            // Set our object's texture to the newly warped image.
            GetComponent<[Renderer](Renderer.html)>().material.mainTexture = destTex;
        }
    }
    

Additional resources: [GetPixel](Texture2D.GetPixel.html).

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

