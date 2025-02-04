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

#  [Mathf](Mathf.html).PerlinNoise

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

[Switch to Manual](../Manual/class-Mathf.html "Go to Mathf Component in the
Manual")

## Declaration

public static float PerlinNoise(float x, float y);

### Parameters

x | X-coordinate of sample point.  
---|---  
y | Y-coordinate of sample point.  
  
### Returns

**float** Value between 0.0 and 1.0. (Return value might be slightly below 0.0
or beyond 1.0.)

### Description

Generate 2D Perlin noise.

Perlin noise is a pseudo-random pattern of float values generated across a 2D
plane (although the technique does generalise to three or more dimensions,
this is not implemented in Unity). The noise does not contain a completely
random value at each point but rather consists of "waves" whose values
gradually increase and decrease across the pattern. The noise can be used as
the basis for texture effects but also for animation, generating terrain
heightmaps and many other things.  
  
![](../StaticFiles/ScriptRefImages/PerlinExample.png)  
_Perlin noise sampled in the range 0..10 (the greyscale values represent
values from 0..1)_  
  
Any point in the plane can be sampled by passing the appropriate X and Y
coordinates. The same coordinates will always return the same sample value but
the plane is essentially infinite so it is easy to avoid repetition by
choosing a random area to sample from.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Create a texture and fill it with Perlin noise.
    // Try varying the xOrg, yOrg and scale values in the inspector
    // while in Play mode to see the effect they have on the noise.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Width and height of the texture in pixels.
        public int pixWidth;
        public int pixHeight;  
      
        // The origin of the sampled area in the plane.
        public float xOrg;
        public float yOrg;  
      
        // The number of cycles of the basic noise pattern that are repeated
        // over the width and height of the texture.
        public float scale = 1.0F;  
      
        private [Texture2D](Texture2D.html) noiseTex;
        private [Color](Color.html)[] pix;
        private [Renderer](Renderer.html) rend;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)>();  
      
            // Set up the texture and a [Color](Color.html) array to hold pixels during processing.
            noiseTex = new [Texture2D](Texture2D.html)(pixWidth, pixHeight);
            pix = new [Color](Color.html)[noiseTex.width * noiseTex.height];
            rend.material.mainTexture = noiseTex;
        }  
      
        void CalcNoise()
        {
            // For each pixel in the texture...
            for (float y = 0.0F; y < noiseTex.height; y++)
            {
                for (float x = 0.0F; x < noiseTex.width; x++)
                {
                    float xCoord = xOrg + x / noiseTex.width * scale;
                    float yCoord = yOrg + y / noiseTex.height * scale;
                    float sample = [Mathf.PerlinNoise](Mathf.PerlinNoise.html)(xCoord, yCoord);
                    pix[(int)y * noiseTex.width + (int)x] = new [Color](Color.html)(sample, sample, sample);
                }
            }  
      
            // Copy the pixel data to the texture and load it into the GPU.
            noiseTex.SetPixels(pix);
            noiseTex.Apply();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            CalcNoise();
        }
    }
    

**Note:** The return value can be slightly lower than 0.0f or slightly higher
than 1.0f. If you need the range of return values to be between 0.0 and 1.0,
clamp the return values.

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

