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

#  [PrefabUtility](PrefabUtility.html).SaveAsPrefabAssetAndConnect

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
SaveAsPrefabAssetAndConnect([GameObject](GameObject.html) instanceRoot, string
assetPath, [InteractionMode](InteractionMode.html) action);

## Declaration

public static [GameObject](GameObject.html)
SaveAsPrefabAssetAndConnect([GameObject](GameObject.html) instanceRoot, string
assetPath, [InteractionMode](InteractionMode.html) action, out bool success);

### Parameters

instanceRoot | The GameObject to save as a Prefab and make into a Prefab instance.  
---|---  
assetPath | The path to save the Prefab at.  
action | The interaction mode to use for this action.  
success | The result of the save action, either successful or unsuccessful. Use this together with the console log to get more insight into the save process.  
  
### Returns

**GameObject** The root GameObject of the saved Prefab Asset, if available.

### Description

Creates a Prefab Asset at the given path from the given GameObject, including
any children in the Scene and at the same time make the given GameObject into
an instance of the new Prefab.

In case some of the children are Prefab instances they will automatically
become nested inside the new Prefab.  
  
The input object must be a plain GameObject or the outermost root of a Prefab
Instance. It cannot be a child inside a Prefab instance.  
  
If the input object is a Prefab instance root the resulting Prefab will be a
Prefab Variant. If you want to create a new unique Prefab instead, you need to
unpack the Prefab instance first.  
  
The returned object is the root GameObject of the saved Prefab Asset, if
available. If the editor is currently in the middle of an asset editing batch
operation, as controlled with
[AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html) and
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html), assets
are not immediately imported upon being saved. In this case, SaveAsPrefabAsset
will return null even if the save was successful because the saved Prefab
Asset was not yet reimported and thus not yet available.  
  
If you are saving over an existing Prefab, Unity tries to preserve references
to the Prefab itself and the individual parts of the Prefab such as child
GameObjects and Components. To do this, it matches the names of GameObjects
between the new saved Prefab and the existing Prefab.  
  
Note: Because this matching is done by name only, if there are multiple
GameObjects with the same name in the Prefab's hierarchy, you cannot predict
which will be matched. Therefore if you need to ensure your references are
preserved when saving over an existing prefab, you must ensure all GameObjects
within the Prefab have unique names.  
  
Also note: You may encounter a similar problem in the case of preserving
references to existing Components when you save over an existing Prefab, if a
single GameObject within the Prefab has more than one of the same Component
type attached. In this case you cannot predict which of them will be matched
to the existing references.  
  
Additional resources:
[PrefabUtility.SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html) and
[Unpacking Prefab instances](../Manual/UnpackingPrefabInstances.html).

    
    
    // This script creates a new menu item Examples>Create Prefab in the main menu.
    // Use it to create Prefab(s) from the selected [GameObject](GameObject.html)(s).
    // Prefab(s) are placed in the "Prefabs" folder.  
      
    using System.IO;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example
    {
        // Creates a new menu item 'Examples > Create Prefab' in the main menu.
        [[MenuItem](MenuItem.html)("Examples/Create Prefab")]
        static void CreatePrefab()
        {
            // Keep track of the currently selected [GameObject](GameObject.html)(s)
            [GameObject](GameObject.html)[] objectArray = [Selection.gameObjects](Selection-gameObjects.html);  
      
            // Loop through every [GameObject](GameObject.html) in the array above
            foreach ([GameObject](GameObject.html) gameObject in objectArray)
            {
                // Create folder Prefabs and set the path as within the Prefabs folder,
                // and name it as the [GameObject](GameObject.html)'s name with the .Prefab format
                if (![Directory.Exists](Windows.Directory.Exists.html)("Assets/Prefabs"))
                    [AssetDatabase.CreateFolder](AssetDatabase.CreateFolder.html)("Assets", "Prefabs");
                string localPath = "Assets/Prefabs/" + gameObject.name + ".prefab";  
      
                // Make sure the file name is unique, in case an existing Prefab has the same name.
                localPath = [AssetDatabase.GenerateUniqueAssetPath](AssetDatabase.GenerateUniqueAssetPath.html)(localPath);  
      
                // Create the new Prefab and log whether Prefab was saved successfully.
                bool prefabSuccess;
                [PrefabUtility.SaveAsPrefabAssetAndConnect](PrefabUtility.SaveAsPrefabAssetAndConnect.html)(gameObject, localPath, [InteractionMode.UserAction](InteractionMode.UserAction.html), out prefabSuccess);
                if (prefabSuccess == true)
                    [Debug.Log](Debug.Log.html)("Prefab was saved successfully");
                else
                    [Debug.Log](Debug.Log.html)("Prefab failed to save" + prefabSuccess);
            }
        }  
      
        // Disable the menu item if no selection is in place.
        [[MenuItem](MenuItem.html)("Examples/Create Prefab", true)]
        static bool ValidateCreatePrefab()
        {
            return [Selection.activeGameObject](Selection-activeGameObject.html) != null && ![EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)([Selection.activeGameObject](Selection-activeGameObject.html));
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

