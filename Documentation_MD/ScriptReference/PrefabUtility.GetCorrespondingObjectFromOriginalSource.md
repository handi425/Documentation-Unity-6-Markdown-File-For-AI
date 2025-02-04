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
[PrefabUtility](PrefabUtility.html).GetCorrespondingObjectFromOriginalSource

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

public static TObject GetCorrespondingObjectFromOriginalSource(TObject
componentOrGameObject);

### Parameters

componentOrGameObject | The object to find the corresponding original object from.  
---|---  
  
### Returns

**TObject** The corresponding object from the original source or null.

### Description

Retrieves the object of origin for the given object.

For any object you pass to this method, Unity follows through the chain of
corresponding objects until there are no more and returns the last one found.  
  
You can use this method to find the corresponding prefab asset where the input
object originated.  
  
For example, in the diagram shown below, prefab asset "A" contains a child
nested prefab "B", which contains a child nested prefab "C".  
  
![](../StaticFiles/ScriptRefImages/nested-prefab-instance-example.png)  
  
Due to this structure, prefab "C" exists in both "A" and "B". It was
_originally added_ in "B", but the last object in the chain is "C"  
  
Therefore in this example scenario, when the GameObject "C (Instance)" is
passed in as the source to this method, this method returns the asset "C".  
  
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
            var o1 = [PrefabUtility.GetCorrespondingObjectFromOriginalSource](PrefabUtility.GetCorrespondingObjectFromOriginalSource.html)(instance);
            [Debug.Log](Debug.Log.html)("Corresponding object from original source: " + o1.name + " from: " + [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(o1));
        }
    }
    

If you need to know the asset where a given GameObject or Component was
originally added (not the last object in the chain), use
[GetOriginalSourceRootWhereGameObjectIsAdded](PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html).  
  
See also:
[GetCorrespondingObjectFromSource](PrefabUtility.GetCorrespondingObjectFromSource.html),
[GetCorrespondingObjectFromSourceAtPath](PrefabUtility.GetCorrespondingObjectFromSourceAtPath.html),
[GetOriginalSourceRootWhereGameObjectIsAdded](PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html).

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

