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

#  [AssetDatabase](AssetDatabase.html).Contains

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

public static bool Contains([Object](Object.html) obj);

## Declaration

public static bool Contains(int instanceID);

### Description

Is object an asset?

Returns true when an object is an asset (corresponds to a file in the Assets
folder), and false if it is not (for example object in the Scene, or an object
created at runtime).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Contains Example")]
        static void ContainsExample()
        {
            //[Material](Material.html) is created in memory and the [Asset](VersionControl.Asset.html) Database does not know about it
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
            [Debug.Log](Debug.Log.html)([AssetDatabase.Contains](AssetDatabase.Contains.html)(material)); //Output will be false
            //[Material](Material.html) is then saved to disk as an asset and therefore [Asset](VersionControl.Asset.html) Database knows that it exists
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(material, "Assets/Materials/MyMaterial.mat");
            [Debug.Log](Debug.Log.html)([AssetDatabase.Contains](AssetDatabase.Contains.html)(material)); //Output will be true
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

