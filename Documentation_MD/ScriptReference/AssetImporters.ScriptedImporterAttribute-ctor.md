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

# ScriptedImporterAttribute Constructor

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

public ScriptedImporterAttribute(int version, string ext);

## Declaration

public ScriptedImporterAttribute(int version, string ext, int
importQueueOffset);

## Declaration

public ScriptedImporterAttribute(int version, string[] exts);

## Declaration

public ScriptedImporterAttribute(int version, string[] exts, string[]
overrideExts);

## Declaration

public ScriptedImporterAttribute(int version, string[] exts, int
importQueueOffset);

## Declaration

public ScriptedImporterAttribute(int version, string[] exts, string[]
overrideExts, int importQueueOffset);

### Parameters

version | A number that is used by the import pipeline to detect new versions of the importer script. Changing this number will trigger a re-import of all assets matching the listed extensions.  
---|---  
exts | List of file name extensions (not including the leading period character) that the scripted importer handles.  
ext | Single file name extension (not including the leading period character) that the scripted importer handles.  
importQueueOffset | Gives control over ordering of asset import based on types. Positive values delay the processing of source asset files while negative values place them earlier in the import process.  
overrideExts | List of file name extensions (not including the leading period character) that the scripted importer can handle in addition to the default file name extension(s).  
  
### Description

Use the ScriptedImporter attribute to register a custom importer derived from
[ScriptedImporter](AssetImporters.ScriptedImporter.html) with Unity's Asset
import pipeline.

Always increment a scripted importer's version number whenever the script
changes. This forces Assets imported with lower version numbers to be re-
imported.  
  
If the Editor's **Auto Refresh** preference is enabled, editing a script
outside of the editor and saving it triggers a re-import of both the script
and all Assets of the corresponding type. The following example declares an
importer that handles files with extension `cb` and `cube`.

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, new[] {"cb", "cube"})]
    public class CubeImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // ...
        }
    }
    

The following example declares an importer that handles files with extension
`sphere`. Its **importQueueOffset** parameter is set to 10, forcing assets
with extension `sphere` to be imported **after** all other scripted importers
that have an **importQueueOffset** of less than 10.

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "sphere", 10)]
    public class SphereImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // ...
        }
    }
    

The following example declares an importer that handles files with the
extension `fbb` and that can be used to import `fbx` files instead of Unity's
default [ModelImporter](ModelImporter.html).

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, new[] {"fbb"}, new[] {"fbx"})]
    public class CustomModelImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // ...
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

