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
[PrefabUtility](PrefabUtility.html).GetOriginalSourceRootWhereGameObjectIsAdded

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

public static [GameObject](GameObject.html)
GetOriginalSourceRootWhereGameObjectIsAdded([GameObject](GameObject.html)
gameObject);

### Parameters

gameObject | GameObject from a Prefab instance or from a Prefab Asset.  
---|---  
  
### Returns

**GameObject** The Prefab Asset root where the input GameObject was added.

### Description

Use this method to find the Prefab Asset root where a Prefab instance or
Prefab Asset object was added originally.

Use this method to find the "original source" where the input object was
added. This is useful in situations where you are working with nested prefabs,
and you need to in which prefab your instance of a nested prefab was
originally added.  
  
For example, in the diagram shown below, prefab asset "A" contains a child
nested prefab "B", which contains a child nested prefab "C".  
  
![](../StaticFiles/ScriptRefImages/nested-prefab-instance-example.png)  
  
Due to this structure, prefab "C" exists in both "A" and "B", however it was
_originally added_ in "B".  
  
Therefore in this example scenario, when the GameObject "C (Instance)" is
passed in as the source to this method, this method returns the asset "B".  
  
The 'Open Prefab' button in the Restructure Dialog uses this method to
determine the correct Prefab Asset to open in Prefab Mode.  
  
The example script below adds a menu item to the editor, which launches a
simple wizard that allows you to test the results of this method.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    public class AssetSourceTestWizard : [ScriptableWizard](ScriptableWizard.html)
    {
        public [GameObject](GameObject.html) instance;  
      
        [[MenuItem](MenuItem.html)("Test/[Asset](VersionControl.Asset.html) Source Test Wizard")]
        static void CreateWizard()
        {
            [ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)<AssetSourceTestWizard>("[Asset](VersionControl.Asset.html) Source Test Wizard", "Do Test");
        }  
      
        void OnWizardCreate()
        {
            var o1 = [PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded](PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html)(instance);
            [Debug.Log](Debug.Log.html)("Original source root where [GameObject](GameObject.html) is added: " + o1.name + " from: " + [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(o1));
        }
    }
    

If you need to know the original source for a given GameObject or Component
(not where it is added) then use
[GetCorrespondingObjectFromOriginalSource](PrefabUtility.GetCorrespondingObjectFromOriginalSource.html).  
  
See also:
[GetCorrespondingObjectFromSource](PrefabUtility.GetCorrespondingObjectFromSource.html),
[GetCorrespondingObjectFromSourceAtPath](PrefabUtility.GetCorrespondingObjectFromSourceAtPath.html),
[GetCorrespondingObjectFromOriginalSource](PrefabUtility.GetCorrespondingObjectFromOriginalSource.html).

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

