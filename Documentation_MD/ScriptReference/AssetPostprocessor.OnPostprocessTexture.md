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
[AssetPostprocessor](AssetPostprocessor.html).OnPostprocessTexture(Texture2D)

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

Add this function to a subclass to get a notification when a texture2D has
completed importing just before Unity compresses it.

You can't choose a compression format at this point. If you want to change
compression format based on filename or other attributes of the texture, use
[AssetPostprocessor.OnPreprocessTexture](AssetPostprocessor.OnPreprocessTexture.html).  
  
However, if you modify the TextureImporter settings in this way, it has no
effect on the texture that Unity is currently importing, but it does apply the
next time Unity imports this texture. This causes unpredictable results.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    // Postprocesses all textures that are placed in a folder
    // "invert color" to have their colors inverted.
    public class InvertColor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPostprocessTexture([Texture2D](Texture2D.html) texture)
        {
            // Only post process textures if they are in a folder
            // "invert color" or a sub folder of it.
            string lowerCaseAssetPath = assetPath.ToLower();
            if (lowerCaseAssetPath.IndexOf("/invert color/") == -1)
                return;  
      
            for (int m = 0; m < texture.mipmapCount; m++)
            {
                [Color](Color.html)[] c = texture.GetPixels(m);  
      
                for (int i = 0; i < c.Length; i++)
                {
                    c[i].r = 1 - c[i].r;
                    c[i].g = 1 - c[i].g;
                    c[i].b = 1 - c[i].b;
                }
                texture.SetPixels(c, m);
            }
            // Instead of setting pixels for each mip map level, you can modify
            // the pixels in the highest mipmap then use texture.Apply(true);
            // to generate lower mip levels.
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

