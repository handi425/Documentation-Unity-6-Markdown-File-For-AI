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

#  [AssetPostprocessor](AssetPostprocessor.html).OnPostprocessCubemap(Cubemap)

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

### Description

Add this function to a subclass to get a notification just before a cubemap
texture has completed importing.

Note that you should avoid modifying the TextureImporter settings in this
manner as it would have no effect on the texture that is currently being
imported but would apply the next time the texture is imported. This behavior
is nondeterministic and therefore undesirable.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    // Postprocesses all cubemaps that are placed in a folder
    // Here we just halve the texels values
    public class ProcessCubemap : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPostprocessCubemap([Cubemap](Cubemap.html) texture)
        {
            string lowerCaseAssetPath = assetPath.ToLower();
            if (lowerCaseAssetPath.IndexOf("/postprocessedcubemaps/") == -1)
                return;  
      
            for (int m = 0; m < texture.mipmapCount; m++)
            {
                for (int face = 0; face < 6; face++)
                {
                    [CubemapFace](CubemapFace.html) f = ([CubemapFace](CubemapFace.html))face;
                    [Color](Color.html)[] c = texture.GetPixels(f, m);  
      
                    for (int i = 0; i < c.Length; i++)
                    {
                        c[i].r = c[i].r * 0.5f;
                        c[i].g = c[i].g * 0.5f;
                        c[i].b = c[i].b * 0.5f;
                    }  
      
                    texture.SetPixels(c, f, m);
                }
                // Instead of setting pixels for each mipmap level, you can also
                // modify only the pixels in the highest mip level. And then simply use
                // texture.Apply(true); to generate lower mip levels.
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

