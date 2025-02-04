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

#  [MonoImporter](MonoImporter.html).SetDefaultReferences

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

public void SetDefaultReferences(string[] name, Object[] target);

### Parameters

name | An array of names of public fields in the imported [MonoScript](MonoScript.html). The type of each field must be derived from UnityEngine.Object.  
---|---  
target | An array of objects to use as default values. The size of the array must match the size of the names array. The array can include null values.  
  
### Description

Sets default references for this [MonoScript](MonoScript.html).

When the Unity Editor instantiates this [MonoScript](MonoScript.html), it uses
the default values to populate the named fields. Additional resources:
[MonoImporter.GetDefaultReference](MonoImporter.GetDefaultReference.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class Example
    {
        [[MenuItem](MenuItem.html)("Examples/Set Default References")]
        public static void SetDefaultReferences()
        {
            var assetPath = "Assets/MyMonoBehaviour.cs";
            var monoImporter = [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)(assetPath) as [MonoImporter](MonoImporter.html);  
      
            var gameObject = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[GameObject](GameObject.html)>([AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)([AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("Cube")[0]));
            var material = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Material](Material.html)>([AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)([AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("defaultMat")[0]));  
      
            var names = new string[] {"MyGameObject", "MyMaterial"};
            var values = new Object[] {gameObject, material};
            monoImporter.SetDefaultReferences(names, values);
            monoImporter.SaveAndReimport();
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

