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

# ScriptedImporterAttribute

class in UnityEditor.AssetImporters

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

Class attribute used to register a custom asset importer derived from
[ScriptedImporter](AssetImporters.ScriptedImporter.html) with Unity's Asset
import pipeline.

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(version: 1, ext: "sphere", AllowCaching = true)]
    public class SphereImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // ...
        }
    }
    

### Properties

[AllowCaching](AssetImporters.ScriptedImporterAttribute.AllowCaching.html)|
Enable cache server uploads and downloads.  
---|---  
[fileExtensions](AssetImporters.ScriptedImporterAttribute-
fileExtensions.html)| The list of file name extensions that this scripted
importer should handle. You must not include the period character, only the
extension characters such as "ext".  
[importQueuePriority](AssetImporters.ScriptedImporterAttribute-
importQueuePriority.html)| Enables controlling the ordering of asset import
based on type. Positive values delay the processing of source asset files
while negative values place them earlier in the import process.  
[overrideFileExtensions](AssetImporters.ScriptedImporterAttribute-
overrideFileExtensions.html)| List of file name extensions (not including the
leading period character) that the scripted importer can handle in addition to
the default file name extension(s).  
[version](AssetImporters.ScriptedImporterAttribute-version.html)| Importer
version number that is used by the import layer to detect new version of the
importer and trigger re-imports when such events occur, to apply latest
changes made to the scripted imrpoter.  
  
### Constructors

[ScriptedImporterAttribute](AssetImporters.ScriptedImporterAttribute-
ctor.html)| Use the ScriptedImporter attribute to register a custom importer
derived from ScriptedImporter with Unity's Asset import pipeline.  
---|---  
  
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

