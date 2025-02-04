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

#  [AssetDatabase](AssetDatabase.html).RemoveObjectFromAsset

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

public static void RemoveObjectFromAsset([Object](Object.html)
objectToRemove);

### Description

Removes object from its asset (Additional resources:
[AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)).

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class Scriptable : [ScriptableObject](ScriptableObject.html)
    {
    }
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Remove Object From [Asset](VersionControl.Asset.html) Example")]
        public static void RemoveObjectFromAssetExample()
        {
            var scriptableObjectList = new List<Scriptable>();  
      
            //Create Scriptable Objects and store them in a List
            for (var i = 0; i < 10; i++)
            {
                scriptableObjectList.Add([ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<Scriptable>());
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(scriptableObjectList[i], $"Assets/ScriptableObjects/SO{i}.asset");
            }  
      
            //Add Materials as Sub Assets to the Scriptable Objects
            foreach (var so in scriptableObjectList)
            {
                [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)(new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard")), so);
            }
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            //Remove Materials from their Scriptable Objects
            foreach (var so in scriptableObjectList)
            {
                var material =
                    [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(so), typeof([Material](Material.html)));
                [AssetDatabase.RemoveObjectFromAsset](AssetDatabase.RemoveObjectFromAsset.html)(material);
            }
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();
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

