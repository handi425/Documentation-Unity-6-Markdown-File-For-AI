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
[AssetImportContext](AssetImporters.AssetImportContext.html).GetOutputArtifactFilePath

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

public string GetOutputArtifactFilePath(string fileName);

### Parameters

fileName | Unique identifier to refer to this Artifact File.  
---|---  
  
### Returns

**string** The file path which can be used to create a new Artifact File.

### Description

Returns the path where to write a new Artifact File with the given fileName.

An Artifact File is part of the result of an importer and can contain any data
that are not UnityEngine.Object. For example the 'info' Artifact File is
reserved by Unity and stores the preview data of the imported Main Object.  
  
The following example shows how to add an Artifact File for a TextureImporter
AssetPostprocessor to save the color of the first pixel of the texture inside
an ArtifactFile. See
[AssetImportContext.GetArtifactFilePath](AssetImporters.AssetImportContext.GetArtifactFilePath.html)
to see how this information can be used by another importer to depends on this
value and not the whole texture.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class SaveFirstPixelColor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        public override uint GetVersion()
        {
            return 1;
        }  
      
        void OnPostprocessTexture([Texture2D](Texture2D.html) texture)
        {
            if (assetPath.StartsWith("Assets/"))
            {
                string path = context.GetOutputArtifactFilePath("firstpixelcolor");
                if (!string.IsNullOrEmpty(path))
                    File.WriteAllText(path, $"#{[ColorUtility.ToHtmlStringRGBA](ColorUtility.ToHtmlStringRGBA.html)(texture.GetPixel(0, 0))}");
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

