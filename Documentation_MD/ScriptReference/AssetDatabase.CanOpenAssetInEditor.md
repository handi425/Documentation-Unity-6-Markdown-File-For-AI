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

#  [AssetDatabase](AssetDatabase.html).CanOpenAssetInEditor

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

public static bool CanOpenAssetInEditor(int instanceID);

### Parameters

instanceID | The instance ID of the asset.  
---|---  
  
### Returns

**bool** Returns true if Unity can successfully open the asset in the Editor,
otherwise returns false.

### Description

Checks if Unity can open an asset in the Editor.

Checks if Unity can open a given asset instance in the Editor if
[AssetDatabase.OpenAsset](AssetDatabase.OpenAsset.html) is executed. Note: The
asset must be written to disk, or this function always returns false.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEngine;  
      
    [CreateAssetMenu(fileName = "MyObject", menuName = "ScriptableObjects/MyObject", order = 1)]
    public class MyObject : [ScriptableObject](ScriptableObject.html)
    {
        public string myData;  
      
        [OnOpenAsset]
        public static bool Open(int instanceID)
        {
            if ([AssetDatabase.GetMainAssetTypeAtPath](AssetDatabase.GetMainAssetTypeAtPath.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(instanceID)) == typeof(MyObject))
            {
                [Debug.Log](Debug.Log.html)("Opening asset");
                return true;
            }
            else  return false; // This method doesn't handle opening of different asset types
        }  
      
        [OnOpenAsset([OnOpenAssetAttributeMode.Validate](Callbacks.OnOpenAssetAttributeMode.Validate.html))]
        public static bool WillOpen(int instanceID)
        {
            if ([AssetDatabase.GetMainAssetTypeAtPath](AssetDatabase.GetMainAssetTypeAtPath.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(instanceID)) == typeof(MyObject))
            {
                // We can open MyObject asset using MyObject opening method
                [Debug.Log](Debug.Log.html)("This asset can be opened by OnOpenAsset marked method");
                return true;
            }
            else  return false; // The passed instance doesn't belong to MyObject type asset so we won't be able to open it using opening method inside MyObject
        }  
      
        [[MenuItem](MenuItem.html)("Test/WillOpenInUnity")]
        public static void WillSelectionBeOpenedInUnity()
        {
            [AssetDatabase.CanOpenAssetInEditor](AssetDatabase.CanOpenAssetInEditor.html)(Selection.activeObject.GetInstanceID());
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

