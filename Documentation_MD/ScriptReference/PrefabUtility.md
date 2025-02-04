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

# PrefabUtility

class in UnityEditor

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

### Description

Utility class for any Prefab related operations.

    
    
    // This script creates a new menu item Examples>Create Prefab in the main menu.
    // Use it to create Prefab(s) from the selected [GameObject](GameObject.html)(s).
    // It is placed in the root Assets folder.
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
    

### Static Properties

[prefabInstanceUpdated](PrefabUtility-prefabInstanceUpdated.html)| Unity calls
this method automatically when Prefab instances in the Scene have been
updated.  
---|---  
  
### Static Methods

[ApplyAddedComponent](PrefabUtility.ApplyAddedComponent.html)| Applies the
added component to the Prefab Asset at the given asset path.  
---|---  
[ApplyAddedGameObject](PrefabUtility.ApplyAddedGameObject.html)| Applies the
added GameObject to the Prefab Asset at the given asset path.  
[ApplyAddedGameObjects](PrefabUtility.ApplyAddedGameObjects.html)| Applies the
added GameObjects to the Prefab Asset at the given asset path.  
[ApplyObjectOverride](PrefabUtility.ApplyObjectOverride.html)| Applies all
overridden properties on a Prefab instance component or GameObject to the
Prefab Asset at the given asset path.  
[ApplyPrefabInstance](PrefabUtility.ApplyPrefabInstance.html)| Applies all
overrides on a Prefab instance to its Prefab Asset.  
[ApplyPrefabInstances](PrefabUtility.ApplyPrefabInstances.html)| Applies all
overrides from a list of Prefab instances to their Prefab Assets.  
[ApplyPropertyOverride](PrefabUtility.ApplyPropertyOverride.html)| Applies a
single overridden property on a Prefab instance to the Prefab Asset at the
given asset path.  
[ApplyRemovedComponent](PrefabUtility.ApplyRemovedComponent.html)| Removes the
component from the Prefab Asset which has the component on it.  
[ApplyRemovedGameObject](PrefabUtility.ApplyRemovedGameObject.html)| Removes
the GameObject from the source Prefab Asset.  
[ConvertToPrefabInstance](PrefabUtility.ConvertToPrefabInstance.html)| Convert
the plain GameObject to a Prefab instance using the provided Prefab Asset root
object.  
[ConvertToPrefabInstances](PrefabUtility.ConvertToPrefabInstances.html)|
Convert an array of GameObjects to Prefab instances of the given Prefab Asset.  
[FindAllInstancesOfPrefab](PrefabUtility.FindAllInstancesOfPrefab.html)|
Retrieves the root GameObjects for all instances of the Prefab asset with root
prefabRoot found in all currently loaded scenes. If prefabRoot is not a valid
Prefab asset root GameObject, an ArgumentException is thrown.  
[GetAddedComponents](PrefabUtility.GetAddedComponents.html)| Retrieves a list
of PrefabUtility.AddedComponent objects which contain information about added
component overrides on the Prefab instance.  
[GetAddedGameObjects](PrefabUtility.GetAddedGameObjects.html)| Retrieves a
list of PrefabUtility.AddedGameObject objects which contain information about
added GameObjects on the Prefab instance.  
[GetCorrespondingObjectFromOriginalSource](PrefabUtility.GetCorrespondingObjectFromOriginalSource.html)|
Retrieves the object of origin for the given object.  
[GetCorrespondingObjectFromSource](PrefabUtility.GetCorrespondingObjectFromSource.html)|
Retrieves the corresponding asset object of source, or null if it can't be
found.  
[GetCorrespondingObjectFromSourceAtPath](PrefabUtility.GetCorrespondingObjectFromSourceAtPath.html)|
Retrieves the corresponding object of the given object from a given Prefab
Asset path.  
[GetIconForGameObject](PrefabUtility.GetIconForGameObject.html)| Retrieves the
icon for the given GameObject.  
[GetNearestPrefabInstanceRoot](PrefabUtility.GetNearestPrefabInstanceRoot.html)|
Retrieves the GameObject that is the root of the nearest Prefab instance the
object is part of.  
[GetObjectOverrides](PrefabUtility.GetObjectOverrides.html)| Retrieves a list
of objects with information about object overrides on the Prefab instance.  
[GetOriginalSourceRootWhereGameObjectIsAdded](PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html)|
Use this method to find the Prefab Asset root where a Prefab instance or
Prefab Asset object was added originally.  
[GetOutermostPrefabInstanceRoot](PrefabUtility.GetOutermostPrefabInstanceRoot.html)|
Retrieves the GameObject that is the root of the outermost Prefab instance the
object is part of.  
[GetPrefabAssetPathOfNearestInstanceRoot](PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot.html)|
Retrieves the asset path of the nearest Prefab instance root the specified
object is part of.  
[GetPrefabAssetType](PrefabUtility.GetPrefabAssetType.html)| Retrieves an enum
value indicating the type of Prefab Asset, such as Regular Prefab, Model
Prefab and Prefab Variant.  
[GetPrefabInstanceHandle](PrefabUtility.GetPrefabInstanceHandle.html)|
Retrieves the PrefabInstance object for the outermost Prefab instance the
provided object is part of.  
[GetPrefabInstanceStatus](PrefabUtility.GetPrefabInstanceStatus.html)|
Determines whether a Prefab instance is properly connected to its asset.  
[GetPropertyModifications](PrefabUtility.GetPropertyModifications.html)|
Returns all modifications that have been applied to a particular Prefab
instance in a Scene or modifications for a Prefab instance in an Asset.See
SetPropertyModifications for details about the fields of the returned
PropertyModification objects.An alternative approach to getting property
overrides information for a Prefab instance is to use the GetObjectOverrides
API which also has Apply and Revert functionality.When using
GetPropertyModifications bear in mind that: it will return both default and
non-default overridesIt can return overrides for all child GameObjects and
their Componentsit can return overrides that are no longer valid.  
[GetRemovedComponents](PrefabUtility.GetRemovedComponents.html)| Returns a
list of objects with information about removed component overrides on the
Prefab instance.  
[GetRemovedGameObjects](PrefabUtility.GetRemovedGameObjects.html)| Returns a
list of objects with information about removed GameObject overrides on the
Prefab instance.  
[HasManagedReferencesWithMissingTypes](PrefabUtility.HasManagedReferencesWithMissingTypes.html)|
Determines whether the object Prefab asset contains any MonoBehaviours with
missing SerializeReference types.  
[HasPrefabInstanceAnyOverrides](PrefabUtility.HasPrefabInstanceAnyOverrides.html)|
Returns true if the given Prefab instance has any overrides.  
[InstantiatePrefab](PrefabUtility.InstantiatePrefab.html)| Instantiates the
given Prefab in a given Scene.  
[IsAddedComponentOverride](PrefabUtility.IsAddedComponentOverride.html)|
Returns true if the given component is added to a Prefab instance as an
override.  
[IsAddedGameObjectOverride](PrefabUtility.IsAddedGameObjectOverride.html)|
Returns true if the given GameObject is added as a child to a Prefab instance
as an override.  
[IsAnyPrefabInstanceRoot](PrefabUtility.IsAnyPrefabInstanceRoot.html)| Is the
GameObject the root of any Prefab instance?  
[IsDefaultOverride](PrefabUtility.IsDefaultOverride.html)| Returns true if the
given modification is considered a default override.  
[IsOutermostPrefabInstanceRoot](PrefabUtility.IsOutermostPrefabInstanceRoot.html)|
Returns true if the given GameObject is an outermost Prefab instance root.  
[IsPartOfAnyPrefab](PrefabUtility.IsPartOfAnyPrefab.html)| Returns true if the
given object is part of a Prefab Asset or Prefab instance.  
[IsPartOfImmutablePrefab](PrefabUtility.IsPartOfImmutablePrefab.html)| Returns
true if the given object is part of a Prefab that cannot be edited.  
[IsPartOfModelPrefab](PrefabUtility.IsPartOfModelPrefab.html)| Returns true if
the given object is part of a Model Prefab Asset or Model Prefab instance.  
[IsPartOfNonAssetPrefabInstance](PrefabUtility.IsPartOfNonAssetPrefabInstance.html)|
Returns true if the given object is part of a Prefab instance that is not part
of a Prefab Asset.  
[IsPartOfPrefabAsset](PrefabUtility.IsPartOfPrefabAsset.html)| Returns true if
the given object is part of a Prefab Asset.  
[IsPartOfPrefabInstance](PrefabUtility.IsPartOfPrefabInstance.html)| Returns
true if the given object is part of a Prefab instance.  
[IsPartOfPrefabThatCanBeAppliedTo](PrefabUtility.IsPartOfPrefabThatCanBeAppliedTo.html)|
Returns true if the given object is part of a Prefab to which overrides can be
applied to.  
[IsPartOfRegularPrefab](PrefabUtility.IsPartOfRegularPrefab.html)| Returns
true if the given object is part of a regular Prefab instance or Prefab Asset.  
[IsPartOfVariantPrefab](PrefabUtility.IsPartOfVariantPrefab.html)| Returns
true if the given object is part of a Prefab Variant Asset or Prefab Variant
instance.  
[IsPrefabAssetMissing](PrefabUtility.IsPrefabAssetMissing.html)| Returns true
if the given object is part of a Prefab instance but the source asset is
missing.  
[LoadPrefabContents](PrefabUtility.LoadPrefabContents.html)| Loads a Prefab
Asset at a given path into an isolated Scene and returns the root GameObject
of the Prefab.  
[LoadPrefabContentsIntoPreviewScene](PrefabUtility.LoadPrefabContentsIntoPreviewScene.html)|
Loads a Prefab Asset at a given path into a given preview Scene and returns
the root GameObject of the Prefab.  
[MergePrefabInstance](PrefabUtility.MergePrefabInstance.html)| Forces a Prefab
instance to merge with changes from the Prefab Asset.  
[RecordPrefabInstancePropertyModifications](PrefabUtility.RecordPrefabInstancePropertyModifications.html)|
Causes modifications made to the Prefab instance to be recorded.  
[RemoveUnusedOverrides](PrefabUtility.RemoveUnusedOverrides.html)| This method
identifies and removes all unused overrides from a list of Prefab Instance
roots. See the manual Unused Overides for more detail.  
[ReplacePrefabAssetOfPrefabInstance](PrefabUtility.ReplacePrefabAssetOfPrefabInstance.html)|
Replace the Prefab Asset for a Prefab instance that exists in a Scene or for a
nested Prefab instance inside another Prefab.  
[ReplacePrefabAssetOfPrefabInstances](PrefabUtility.ReplacePrefabAssetOfPrefabInstances.html)|
Replace the Prefab Asset for an array of Prefab instances that exists in
Scenes or for nested Prefab instances inside another Prefab.  
[RevertAddedComponent](PrefabUtility.RevertAddedComponent.html)| Removes this
added component on a Prefab instance.  
[RevertAddedGameObject](PrefabUtility.RevertAddedGameObject.html)| Removes
this added GameObject from a Prefab instance.  
[RevertObjectOverride](PrefabUtility.RevertObjectOverride.html)| Reverts all
overridden properties on a Prefab instance component or GameObject.  
[RevertPrefabInstance](PrefabUtility.RevertPrefabInstance.html)| Reverts all
overrides on a Prefab instance.  
[RevertPropertyOverride](PrefabUtility.RevertPropertyOverride.html)| Reverts a
single property override on a Prefab instance.  
[RevertRemovedComponent](PrefabUtility.RevertRemovedComponent.html)| Adds this
removed component back on the Prefab instance.  
[RevertRemovedGameObject](PrefabUtility.RevertRemovedGameObject.html)| Adds
this removed GameObject back on the Prefab instance.  
[SaveAsPrefabAsset](PrefabUtility.SaveAsPrefabAsset.html)| Creates a Prefab
Asset at the given path from the given GameObject, including any childen in
the Scene without modifying the input objects.  
[SaveAsPrefabAssetAndConnect](PrefabUtility.SaveAsPrefabAssetAndConnect.html)|
Creates a Prefab Asset at the given path from the given GameObject, including
any children in the Scene and at the same time make the given GameObject into
an instance of the new Prefab.  
[SavePrefabAsset](PrefabUtility.SavePrefabAsset.html)| Saves the version of an
existing Prefab Asset that exists in memory back to disk.  
[SetPropertyModifications](PrefabUtility.SetPropertyModifications.html)|
Assigns a set of PropertyModification objects to a target Prefab instance
relative to its source Prefab Asset.  
[UnloadPrefabContents](PrefabUtility.UnloadPrefabContents.html)| Releases the
content from a Prefab previously loaded with LoadPrefabContents from memory.  
[UnpackAllInstancesOfPrefab](PrefabUtility.UnpackAllInstancesOfPrefab.html)|
Unpacks all instances of a given Prefab Asset root GameObject in all open
scenes so that all instances are replaced with the contents of the Prefab
Asset while retaining all override values.  
[UnpackPrefabInstance](PrefabUtility.UnpackPrefabInstance.html)| Unpacks a
given Prefab instance so that it is replaced with the contents of the Prefab
Asset while retaining all override values.  
[UnpackPrefabInstanceAndReturnNewOutermostRoots](PrefabUtility.UnpackPrefabInstanceAndReturnNewOutermostRoots.html)|
Unpacks the given Prefab instance using the behaviour specified by unpackMode.  
  
### Events

[prefabInstanceApplied](PrefabUtility-prefabInstanceApplied.html)| Unity calls
this method automatically after a Prefab instance has been applied.  
---|---  
[prefabInstanceApplying](PrefabUtility-prefabInstanceApplying.html)| Unity
calls this method automatically before a Prefab instance is applied.  
[prefabInstanceReverted](PrefabUtility-prefabInstanceReverted.html)| Unity
calls this method automatically after a Prefab instance has been reverted.  
[prefabInstanceReverting](PrefabUtility-prefabInstanceReverting.html)| Unity
calls this method automatically before a Prefab instance is reverted.  
[prefabInstanceUnpacked](PrefabUtility-prefabInstanceUnpacked.html)| Unity
calls this method automatically after a Prefab instance is unpacked.  
[prefabInstanceUnpacking](PrefabUtility-prefabInstanceUnpacking.html)| Unity
calls this method automatically before a Prefab instance is unpacked.  
  
### Delegates

[PrefabInstanceUpdated](PrefabUtility.PrefabInstanceUpdated.html)| Delegate
for method that is called after Prefab instances in the Scene have been
updated.  
---|---  
  
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

