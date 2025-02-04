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

#  [PrefabUtility](PrefabUtility.html).GetCorrespondingObjectFromSourceAtPath

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

public static TObject GetCorrespondingObjectFromSourceAtPath(TObject
componentOrGameObject, string assetPath);

### Parameters

componentOrGameObject | The object to find the corresponding object from.  
---|---  
assetPath | The asset path of the Prefab Asset to get the corresponding object from.  
  
### Returns

**TObject** The corresponding object or null.

### Description

Retrieves the corresponding object of the given object from a given Prefab
Asset path.

Use this method to find the corresponding asset the `source` was instantiated
from, if but only if it is within the prefab asset at the specified path.  
  
If you don't have the path to pass in, you can use
[GetCorrespondingObjectFromSource](PrefabUtility.GetCorrespondingObjectFromSource.html)
instead.  
  
This method returns null if the given object does not have a corresponding
object within the prefab asset at the specified path.  
  
For example, in the diagram shown below, prefab asset "A" contains a child
nested prefab "B", which contains a child nested prefab "C".  
  
![](../StaticFiles/ScriptRefImages/nested-prefab-instance-example.png)  
  
In this example scenario, when the GameObject "C (Instance)" is passed in as
the source to this method, and "Assets/A.prefab" is passed as the path, this
method returns the object "C (Nested Prefab)" from the prefab asset "A".  
  
The example script below adds a menu item to the editor, which launches a
simple wizard that allows you to test the results of this method.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    public class AssetSourceTestWizard : [ScriptableWizard](ScriptableWizard.html)
    {
        public [GameObject](GameObject.html) instance;
        public string path;  
      
        [[MenuItem](MenuItem.html)("Test/[Asset](VersionControl.Asset.html) Source Test Wizard")]
        static void CreateWizard()
        {
            [ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)<AssetSourceTestWizard>("[Asset](VersionControl.Asset.html) Source Test Wizard", "Do Test");
        }  
      
        void OnWizardCreate()
        {
            var o1 = [PrefabUtility.GetCorrespondingObjectFromSourceAtPath](PrefabUtility.GetCorrespondingObjectFromSourceAtPath.html)(instance, path);
            [Debug.Log](Debug.Log.html)("Corresponding object from source: " + o1.name);
        }
    }
    

See also:
[GetCorrespondingObjectFromSource](PrefabUtility.GetCorrespondingObjectFromSource.html),
[GetOriginalSourceRootWhereGameObjectIsAdded](PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html),
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

