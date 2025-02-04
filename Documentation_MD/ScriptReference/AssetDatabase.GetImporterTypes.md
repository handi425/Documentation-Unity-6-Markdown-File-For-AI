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

#  [AssetDatabase](AssetDatabase.html).GetImporterTypes

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

public static Type[] GetImporterTypes(ReadOnlySpan<GUID> guids);

### Parameters

guids | Array of asset GUIDs to check. The importer type for each asset in the array is returned.  
---|---  
  
### Description

Returns the types of importers associated with the specified array of assets,
without loading those assets.

This method is a batch version of
[AssetDatabase.GetImporterType](AssetDatabase.GetImporterType.html). Use this
method if you need to check a large number of asset importers at once.
**Note** : GUID Arrays can be implicitly cast to ReadOnlySpan, see example for
usage.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AssetDatabaseExamples
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/GetMatchingAssetTypes")]
        public static void GetMatchingAssetTypes()
        {
            var matchingAssets = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("Powerup");
            GUID[] guids = new GUID[matchingAssets.Length];  
      
            for(int i = 0; i < guids.Length; ++i)
            {
                guids[i] = new GUID(matchingAssets[i]);
            }  
      
            var matchingTypes = [AssetDatabase.GetImporterTypes](AssetDatabase.GetImporterTypes.html)(guids);  
      
            foreach (var curType in matchingTypes)
            {
                [Debug.Log](Debug.Log.html)($"Importer type: {curType}");
            }
        }
    }

* * *

## Declaration

public static Type[] GetImporterTypes(string[] paths);

### Parameters

paths | Array of asset paths to check. The importer type for each asset in the array is returned.  
---|---  
  
### Description

Returns the types of importers associated with the specified array of assets,
without loading those assets.

The asset paths you provide should be relative to the project folder root. For
example, "Assets/MyTextures/hello.png". This method is a batch version of
[AssetDatabase.GetImporterType](AssetDatabase.GetImporterType.html). Use this
method if you need to check a large number of asset importers at once.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AssetDatabaseExamples
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/GetImporterTypeOfSelectedObjects")]
        public static void GetImporterTypeOfSelectedObjects()
        {
            var selectedObjects = [Selection.objects](Selection-objects.html);
            string[] paths = new string[selectedObjects.Length];  
      
            for (int i = 0; i < paths.Length; ++i)
            {
                paths[i] = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(selectedObjects[i]);
            }  
      
            var selectedObjectTypes = [AssetDatabase.GetImporterTypes](AssetDatabase.GetImporterTypes.html)(paths);  
      
            foreach (var curType in selectedObjectTypes)
            {
                [Debug.Log](Debug.Log.html)($"Importer type: {curType}");
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

