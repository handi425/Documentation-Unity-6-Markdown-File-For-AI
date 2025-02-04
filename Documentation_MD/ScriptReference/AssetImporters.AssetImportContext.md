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

# AssetImportContext

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

Defines the import context for scripted importers during an import event.

This class carries both input and output information for the OnImportAsset()
task.

### Properties

[assetPath](AssetImporters.AssetImportContext-assetPath.html)| The path of the
source asset file to be imported.  
---|---  
[mainObject](AssetImporters.AssetImportContext-mainObject.html)| The main
object set on the AssetImportContext.  
[selectedBuildTarget](AssetImporters.AssetImportContext-
selectedBuildTarget.html)| Returns the current build target and creates a
dependency on the target platform within a scripted importer.  
  
### Public Methods

[AddObjectToAsset](AssetImporters.AssetImportContext.AddObjectToAsset.html)|
Adds an object to the result of the import operation.  
---|---  
[DependsOnArtifact](AssetImporters.AssetImportContext.DependsOnArtifact.html)|
Setup artifact dependency to an asset.  
[DependsOnCustomDependency](AssetImporters.AssetImportContext.DependsOnCustomDependency.html)|
Allows you to specify that an Asset has a custom dependency.  
[DependsOnSourceAsset](AssetImporters.AssetImportContext.DependsOnSourceAsset.html)|
Allows you to specify that an Asset depends directly on the source file of
another Asset (as opposed to the import result of another asset).  
[GetArtifactFilePath](AssetImporters.AssetImportContext.GetArtifactFilePath.html)|
Returns the path of the Artifact file that was created by another importer,
and adds a dependency to that file.  
[GetObjects](AssetImporters.AssetImportContext.GetObjects.html)| Gets the list
of objects set on the AssetImportContext.  
[GetOutputArtifactFilePath](AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html)|
Returns the path where to write a new Artifact File with the given fileName.  
[GetReferenceToAssetMainObject](AssetImporters.AssetImportContext.GetReferenceToAssetMainObject.html)|
Returns the main asset from the given path (if it exists) and automatically
adds a dependency on its path if it is the main asset type.  
[LogImportError](AssetImporters.AssetImportContext.LogImportError.html)| Logs
an error message encountered during import.  
[LogImportWarning](AssetImporters.AssetImportContext.LogImportWarning.html)|
Logs a warning message encountered during import.  
[SetMainObject](AssetImporters.AssetImportContext.SetMainObject.html)| Sets
the main object for import.  
  
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

