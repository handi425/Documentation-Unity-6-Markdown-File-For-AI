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

#  [PrefabUtility](PrefabUtility.html).MergePrefabInstance

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

public static void MergePrefabInstance([GameObject](GameObject.html)
instanceRoot);

### Parameters

instanceRoot | Root of Prefab instance to update.  
---|---  
  
### Description

Forces a Prefab instance to merge with changes from the Prefab Asset.

Unity will in most cases handle re-merging of the Prefab instance when you
make changes in the Editor or via scripting. However, as shown in the example
below, there are some rare cases where editing a Prefab instance from script
requires you to force merge the instance to get immediate updates.  
  
If you do not call MergePrefabInstance in those rare cases the re-merge will
happen automatically at the end of the current frame, but if you need the
changes reflected immediately in your script you have to force the merge.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // This example shows how to use [PrefabUtility.MergePrefabInstance](PrefabUtility.MergePrefabInstance.html) to force update an instance after some changes  
      
    public class SuppressedComponentExample
    {
        public static void MergePrefabInstanceExample()
        {
            var instance = new [GameObject](GameObject.html)("MyPrefabInstance");
            const string path = "Assets/MyPrefab.prefab";
            var prefab = [PrefabUtility.SaveAsPrefabAssetAndConnect](PrefabUtility.SaveAsPrefabAssetAndConnect.html)(instance, path, [InteractionMode.AutomatedAction](InteractionMode.AutomatedAction.html));  
      
            // Add [Component](Component.html) to instance
            var component = instance.AddComponent<[Rigidbody](Rigidbody.html)>();  
      
            // Add same type of component to the Prefab asset
            using (var scope = new [PrefabUtility.EditPrefabContentsScope](PrefabUtility.EditPrefabContentsScope.html)(path))
            {
                scope.prefabContentsRoot.AddComponent<[Rigidbody](Rigidbody.html)>();
            }  
      
            // Because a [Rigidbody](Rigidbody.html) already exists on the Prefab instance the one from the asset will be suppressed
            // we can get the suppressor and verify this
            var suppressor = instance.GetComponent<[Rigidbody](Rigidbody.html)>();
            [Debug.Log](Debug.Log.html)($"Is component part of the Prefab instance: {[PrefabUtility.IsPartOfPrefabInstance](PrefabUtility.IsPartOfPrefabInstance.html)(suppressor)}");  
      
            // Destroy the suppressor to make the suppressed object return to glory
            [Undo.DestroyObjectImmediate](Undo.DestroyObjectImmediate.html)(suppressor);
            [PrefabUtility.MergePrefabInstance](PrefabUtility.MergePrefabInstance.html)(instance);  
      
            // Now we will get the former suppressed component and verify that it is actually part of the prefab
            var formerSuppressed = instance.GetComponent<[Rigidbody](Rigidbody.html)>();
            [Debug.Log](Debug.Log.html)($"Is component part of the Prefab instance: {[PrefabUtility.IsPartOfPrefabInstance](PrefabUtility.IsPartOfPrefabInstance.html)(formerSuppressed)}");
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

