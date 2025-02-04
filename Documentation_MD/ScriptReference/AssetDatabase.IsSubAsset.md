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

#  [AssetDatabase](AssetDatabase.html).IsSubAsset

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

public static bool IsSubAsset([Object](Object.html) obj);

## Declaration

public static bool IsSubAsset(int instanceID);

### Parameters

obj | The asset Object to query.  
---|---  
instanceID | Instance ID of the asset Object to query.  
  
### Description

Does the asset form part of another asset?

Some assets may form part of another asset (for example, a procedural material
can be part of a material package). This function tells if an asset is
subordinated in this way.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    public class Scriptable : [ScriptableObject](ScriptableObject.html)
    {
    }  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Is Sub [Asset](VersionControl.Asset.html) Example")]
        static void IsSubAssetExample()
        {
            var materialAsset = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            //materialAsset is still in memory, therefore this will be False
            [Debug.Log](Debug.Log.html)([AssetDatabase.IsSubAsset](AssetDatabase.IsSubAsset.html)(materialAsset));  
      
            //Create a Scriptable object
            var scriptableAssetPath = "Assets/ScriptableObjects/NewObject.asset";
            var mainAsset = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<Scriptable>();
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(mainAsset, scriptableAssetPath);  
      
            //Add the [Material](Material.html) [Asset](VersionControl.Asset.html) to the Scriptable object, so that the [Material](Material.html) becomes a Sub [Asset](VersionControl.Asset.html) of the Scriptable object
            [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)(materialAsset, scriptableAssetPath);
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            //This will be True because the [Material](Material.html) asset has been added to the mainAsset and is now a Sub [Asset](VersionControl.Asset.html)
            [Debug.Log](Debug.Log.html)([AssetDatabase.IsSubAsset](AssetDatabase.IsSubAsset.html)(materialAsset));
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

