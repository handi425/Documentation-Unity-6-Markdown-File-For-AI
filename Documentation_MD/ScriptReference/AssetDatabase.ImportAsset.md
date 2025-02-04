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

#  [AssetDatabase](AssetDatabase.html).ImportAsset

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

public static void ImportAsset(string path,
[ImportAssetOptions](ImportAssetOptions.html) options =
ImportAssetOptions.Default);

### Description

Import asset at path.

This imports an Asset at the specified path, and triggers a number of
callbacks including
[AssetModificationProcessor.OnWillSaveAssets](AssetModificationProcessor.OnWillSaveAssets.html)
and
[AssetPostprocessor.OnPostprocessAllAssets](AssetPostprocessor.OnPostprocessAllAssets.html)  
  
All paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png"  
  
Additional resources: [ImportAssetOptions](ImportAssetOptions.html).

    
    
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ImportAssetExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("APIExamples/ImportAsset")]
        static void ImportAssetOnlyImportsSingleAsset()
        {
            string[] fileNames = new[] { "test_file01.txt", "test_file02.txt" };  
      
            for (int i = 0; i < fileNames.Length; ++i)
            {
                var unimportedFileName = fileNames[i];
                var assetsPath = [Application.dataPath](Application-dataPath.html) + "/Artifacts/" + unimportedFileName;
                File.WriteAllText(assetsPath, "Testing 123");
            }  
      
            var relativePath = "Assets/Artifacts/test_file01.txt";
            [AssetDatabase.ImportAsset](AssetDatabase.ImportAsset.html)(relativePath);
        }
    }  
      
    public class PostProcessImportAsset : [AssetPostprocessor](AssetPostprocessor.html)
    {
        //Based on this example, the output from this function should be:
        //  OnPostprocessAllAssets
        //  Imported: Assets/Artifacts/test_file01.txt
        //
        //test_file02.txt should not even show up on the Project Browser
        //until a refresh happens.
        static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)
        {
            [Debug.Log](Debug.Log.html)("OnPostprocessAllAssets");  
      
            foreach (var imported in importedAssets)
                [Debug.Log](Debug.Log.html)("Imported: " + imported);  
      
            foreach (var deleted in deletedAssets)
                [Debug.Log](Debug.Log.html)("Deleted: " + deleted);  
      
            foreach (var moved in movedAssets)
                [Debug.Log](Debug.Log.html)("Moved: " + moved);  
      
            foreach (var movedFromAsset in movedFromAssetPaths)
                [Debug.Log](Debug.Log.html)("Moved from [Asset](VersionControl.Asset.html): " + movedFromAsset);
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

