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
[AssetImportContext](AssetImporters.AssetImportContext.html).GetArtifactFilePath

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

public string GetArtifactFilePath(GUID guid, string fileName);

## Declaration

public string
GetArtifactFilePath([Experimental.ArtifactKey](Experimental.ArtifactKey.html)
key, string fileName);

### Parameters

guid | The guid of the Artifact File dependency.  
---|---  
key | The Artifact key of the Artifact File dependency.  
fileName | The name of the Artifact File to depend upon. See [[AssetImportContext.GetOutputArtifactFilePath.  
  
### Returns

**string** The path inside the Library folder from which you can read the
content of the requested Artifact File.

### Description

Returns the path of the Artifact file that was created by another importer,
and adds a dependency to that file.

This method must be used in conjunction with
[AssetImportContext.GetOutputArtifactFilePath](AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html).
Once an Artifact File has been created by another importer, using this method
will return this Artifact File path and add a dependency to it. It is then
possible to read this Artifact File's content to generate the import result.
The following example shows a ScriptedImporter generating a Material and
setting its base color using the first pixel color saved in an Artifact File
from the example inside
[AssetImportContext.GetOutputArtifactFilePath](AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html).
Note: While there is no limit on how many Artifact Files are created using
[AssetImportContext.GetOutputArtifactFilePath](AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html),
it is only possible to depends upon the first 32 Artifact Files created by a
single Asset import.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using UnityEngine;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "pixelMat", 1, AllowCaching = true)]
    public class MaterialFromFirstPixel : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public LazyLoadReference<[Texture2D](Texture2D.html)> m_Texture;  
      
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var color = [Color.magenta](Color-magenta.html);
            if ([AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(m_Texture, out var stringGuid, out var id))
            {
                string path = string.Empty;
                if (GUID.TryParse(stringGuid, out var guid))
                    path = ctx.GetArtifactFilePath(guid, "firstpixelcolor");
                else
                    path = ctx.GetArtifactFilePath([AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(stringGuid), "firstpixelcolor");
                if (!string.IsNullOrEmpty(path))
                {
                    var colorString = File.ReadAllText(path);
                    [ColorUtility.TryParseHtmlString](ColorUtility.TryParseHtmlString.html)(colorString, out color);
                }
            }  
      
            var mat = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            mat.color = color;
            ctx.AddObjectToAsset("main", mat);
            ctx.SetMainObject(mat);
        }
    }
    

* * *

## Declaration

public string GetArtifactFilePath(string path, string fileName);

### Parameters

path | The path of the Asset whose Artifact File should be the dependency. Note: Although the dependency is the Artifact File (import result) which is stored in the library folder, this parameter is the path to the Asset in the Assets folder, and _not_ a path to the Artifact File in the Library folder.  
---|---  
fileName | The name of the Artifact File to depend upon. See [[AssetImportContext.GetOutputArtifactFilePath.  
  
### Returns

**string** The path inside the Library folder from which you can read the
content of the requested Artifact File.

### Description

Returns the path of the Artifact file that was created by another importer,
and adds a dependency to that file and the source asset path.

In addition to creating a dependency on the import artifact, this overload of
the method also adds a dependency to the asset's path. This means if you
rename or move the asset that created the artifact File in the project, Unity
will re-import the asset, even if the artifact file is unchanged. This can be
useful if you want to implement a functional naming convention as part of your
asset import processing. Use the GUID or ArtifactKey overload to avoid
depending on the asset path if you do not want this.

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

