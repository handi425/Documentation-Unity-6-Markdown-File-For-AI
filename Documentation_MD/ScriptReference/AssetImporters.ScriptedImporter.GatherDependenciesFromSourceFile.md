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
[AssetImporters.ScriptedImporter](AssetImporters.ScriptedImporter.html).GatherDependenciesFromSourceFile(string)

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

### Parameters

path | The path of the asset currently being processed by this method.  
---|---  
  
### Returns

**void** A string array containing paths to the assets that you want create
dependencies on for the asset currently being processed by this method.

### Description

A static callback that you can implement to set up artifact dependencies to
other Assets, and optimize the order your assets are imported.

If you implement this method in a class inheriting from ScriptedImporter, it
will be called for all Assets that your class is configured to import, before
the importing starts.  
  
Your ScriptedImporter class can then return an array of paths to other Assets
that the Asset depends on the import result from (which might depend on how
your ScriptedImporter interprets the contents of the file that it is
importing).  
  
Unity uses the information you return from this method to import assets in the
most efficient order, avoiding the need to re-import assets multiple times
where possible.  
  
Note: Each type of importer has a specific priority in the import process. If
you specify an asset dependency that belongs to a different import priority,
it will not override the import priority, and therefore a repeat import can
still occur.  
  
For more information about artifact dependencies check
[AssetImportContext.DependsOnArtifact](AssetImporters.AssetImportContext.DependsOnArtifact.html).
For the dependencies reported using GatherDependenciesFromSourceFile, there is
no need to report them again with AssetImportContext.DependsOnArtifact. It
however valid to add more artifact dependencies that may be discovered during
the actual import.  
  
**Note:**  
In your implementation of this method, or any methods that you call from your
implementation, you must not call any of the following APIs:  
  
[AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)  
  
[AssetDatabase.LoadAllAssetRepresentationsAtPath](AssetDatabase.LoadAllAssetRepresentationsAtPath.html)  
  
[AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html)  
  
[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)  
  
[AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)  
  
Unity throws an exception if you call any of the above methods from your
implementation of this method.

    
    
    using UnityEditor.AssetImporters;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "my_asset_type", AllowCaching = true)]
    class MyAssetImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        static string[] GatherDependenciesFromSourceFile(string path)
        {
            // Called before actual import for each changed asset that is imported by this importer type (assets having "my_asset_type" file extension in this example)
            // Extract the dependencies for the asset specified in path.
            // For asset dependencies that are discovered, return them in the string array, where the string is the path to asset
        }  
      
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // There is no need to call ctx.DependsOnArtfact for the dependencies reported in GatherDependenciesFromSourceFile.
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

