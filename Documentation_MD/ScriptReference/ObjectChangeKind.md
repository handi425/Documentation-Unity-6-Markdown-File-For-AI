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

# ObjectChangeKind

enumeration

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

This enumeration describes the different kind of changes that can be tracked
in an [ObjectChangeEventStream](ObjectChangeEventStream.html). Each event has
a corresponding type in [ObjectChangeEvents](ObjectChangeEvents.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [InitializeOnLoad]
    public class ObjectChangeEventsExample
    {
        static ObjectChangeEventsExample()
        {
            [ObjectChangeEvents.changesPublished](ObjectChangeEvents-changesPublished.html) += ChangesPublished;
        }  
      
        static void ChangesPublished(ref [ObjectChangeEventStream](ObjectChangeEventStream.html) stream)
        {
            for (int i = 0; i < stream.length; ++i)
            {
                var type = stream.GetEventType(i);
                switch (type)
                {
                    case [ObjectChangeKind.ChangeScene](ObjectChangeKind.ChangeScene.html):
                        stream.GetChangeSceneEvent(i, out var changeSceneEvent);
                        [Debug.Log](Debug.Log.html)($"{type}: {changeSceneEvent.scene}");
                        break;  
      
                    case [ObjectChangeKind.CreateGameObjectHierarchy](ObjectChangeKind.CreateGameObjectHierarchy.html):
                        stream.GetCreateGameObjectHierarchyEvent(i, out var createGameObjectHierarchyEvent);
                        var newGameObject = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(createGameObjectHierarchyEvent.instanceId) as [GameObject](GameObject.html);
                        [Debug.Log](Debug.Log.html)($"{type}: {newGameObject} in scene {createGameObjectHierarchyEvent.scene}.");
                        break;  
      
                    case [ObjectChangeKind.ChangeGameObjectStructureHierarchy](ObjectChangeKind.ChangeGameObjectStructureHierarchy.html):
                        stream.GetChangeGameObjectStructureHierarchyEvent(i, out var changeGameObjectStructureHierarchy);
                        var gameObject = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeGameObjectStructureHierarchy.instanceId) as [GameObject](GameObject.html);
                        [Debug.Log](Debug.Log.html)($"{type}: {gameObject} in scene {changeGameObjectStructureHierarchy.scene}.");
                        break;  
      
                    case [ObjectChangeKind.ChangeGameObjectStructure](ObjectChangeKind.ChangeGameObjectStructure.html):
                        stream.GetChangeGameObjectStructureEvent(i, out var changeGameObjectStructure);
                        var gameObjectStructure = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeGameObjectStructure.instanceId) as [GameObject](GameObject.html);
                        [Debug.Log](Debug.Log.html)($"{type}: {gameObjectStructure} in scene {changeGameObjectStructure.scene}.");
                        break;  
      
                    case [ObjectChangeKind.ChangeGameObjectParent](ObjectChangeKind.ChangeGameObjectParent.html):
                        stream.GetChangeGameObjectParentEvent(i, out var changeGameObjectParent);
                        var gameObjectChanged = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeGameObjectParent.instanceId) as [GameObject](GameObject.html);
                        var newParentGo = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeGameObjectParent.newParentInstanceId) as [GameObject](GameObject.html);
                        var previousParentGo = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeGameObjectParent.previousParentInstanceId) as [GameObject](GameObject.html);
                        [Debug.Log](Debug.Log.html)($"{type}: {gameObjectChanged} from {previousParentGo} to {newParentGo} from scene {changeGameObjectParent.previousScene} to scene {changeGameObjectParent.newScene}.");
                        break;  
      
                    case [ObjectChangeKind.ChangeGameObjectOrComponentProperties](ObjectChangeKind.ChangeGameObjectOrComponentProperties.html):
                        stream.GetChangeGameObjectOrComponentPropertiesEvent(i, out var changeGameObjectOrComponent);
                        var goOrComponent = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeGameObjectOrComponent.instanceId);
                        if (goOrComponent is [GameObject](GameObject.html) go)
                        {
                            [Debug.Log](Debug.Log.html)($"{type}: [GameObject](GameObject.html) {go} change properties in scene {changeGameObjectOrComponent.scene}.");
                        }
                        else if (goOrComponent is [Component](Component.html) component)
                        {
                            [Debug.Log](Debug.Log.html)($"{type}: [Component](Component.html) {component} change properties in scene {changeGameObjectOrComponent.scene}.");
                        }
                        break;  
      
                    case [ObjectChangeKind.DestroyGameObjectHierarchy](ObjectChangeKind.DestroyGameObjectHierarchy.html):
                        stream.GetDestroyGameObjectHierarchyEvent(i, out var destroyGameObjectHierarchyEvent);
                        // The destroyed [GameObject](GameObject.html) can not be converted with [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html) as it has already been destroyed.
                        var destroyParentGo = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(destroyGameObjectHierarchyEvent.parentInstanceId) as [GameObject](GameObject.html);
                        [Debug.Log](Debug.Log.html)($"{type}: {destroyGameObjectHierarchyEvent.instanceId} with parent {destroyParentGo} in scene {destroyGameObjectHierarchyEvent.scene}.");
                        break;  
      
                    case [ObjectChangeKind.CreateAssetObject](ObjectChangeKind.CreateAssetObject.html):
                        stream.GetCreateAssetObjectEvent(i, out var createAssetObjectEvent);
                        var createdAsset = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(createAssetObjectEvent.instanceId);
                        var createdAssetPath = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(createAssetObjectEvent.guid);
                        [Debug.Log](Debug.Log.html)($"{type}: {createdAsset} at {createdAssetPath} in scene {createAssetObjectEvent.scene}.");
                        break;  
      
                    case [ObjectChangeKind.DestroyAssetObject](ObjectChangeKind.DestroyAssetObject.html):
                        stream.GetDestroyAssetObjectEvent(i, out var destroyAssetObjectEvent);
                        // The destroyed asset can not be converted with [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html) as it has already been destroyed.
                        [Debug.Log](Debug.Log.html)($"{type}: Instance Id {destroyAssetObjectEvent.instanceId} with Guid {destroyAssetObjectEvent.guid} in scene {destroyAssetObjectEvent.scene}.");
                        break;  
      
                    case [ObjectChangeKind.ChangeAssetObjectProperties](ObjectChangeKind.ChangeAssetObjectProperties.html):
                        stream.GetChangeAssetObjectPropertiesEvent(i, out var changeAssetObjectPropertiesEvent);
                        var changeAsset = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(changeAssetObjectPropertiesEvent.instanceId);
                        var changeAssetPath = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(changeAssetObjectPropertiesEvent.guid);
                        [Debug.Log](Debug.Log.html)($"{type}: {changeAsset} at {changeAssetPath} in scene {changeAssetObjectPropertiesEvent.scene}.");
                        break;  
      
                    case [ObjectChangeKind.UpdatePrefabInstances](ObjectChangeKind.UpdatePrefabInstances.html):
                        stream.GetUpdatePrefabInstancesEvent(i, out var updatePrefabInstancesEvent);
                        string s = "";
                        s += $"{type}: scene {updatePrefabInstancesEvent.scene}. Instances ({updatePrefabInstancesEvent.instanceIds.Length}):\n";
                        foreach (var prefabId in updatePrefabInstancesEvent.instanceIds)
                        {
                            s += [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(prefabId).ToString() + "\n";
                        }
                        [Debug.Log](Debug.Log.html)(s);
                        break;
                }
            }
        }
    }
    

### Properties

[None](ObjectChangeKind.None.html)| Indicates an uninitialized value.  
---|---  
[ChangeScene](ObjectChangeKind.ChangeScene.html)| A change of this type
indicates that an open scene has been changed ("dirtied") without any more
specific information available. This happens for example when
EditorSceneManager.MarkSceneDirty is used.  
[CreateGameObjectHierarchy](ObjectChangeKind.CreateGameObjectHierarchy.html)|
A change of this type indicates that a GameObject has been created, possibly
with additional objects below it in the hierarchy. This happens for example
when Undo.RegisterCreatedObjectUndo is used with a GameObject.  
[ChangeGameObjectStructureHierarchy](ObjectChangeKind.ChangeGameObjectStructureHierarchy.html)|
A change of this type indicates that the structure of a GameObject has changed
and any GameObject in the hierarchy below it might have changed. This happens
for example when Undo.RegisterFullObjectHierarchyUndo is used.  
[ChangeGameObjectStructure](ObjectChangeKind.ChangeGameObjectStructure.html)|
A change of this type indicates that the structure of a GameObject has
changed. This happens when a component is added to or removed from the
GameObject using Undo.AddComponent or Undo.DestroyObjectImmediate.  
[ChangeGameObjectParent](ObjectChangeKind.ChangeGameObjectParent.html)| A
change of this type indicates that the parent of a GameObject has changed.
This happens when Undo.SetTransformParent or
SceneManager.MoveGameObjectToScene is used.  
[ChangeGameObjectOrComponentProperties](ObjectChangeKind.ChangeGameObjectOrComponentProperties.html)|
A change of this type indicates that a property of a GameObject or Component
has changed. This happens for example when Undo.RecordObject is used with an
instance of a Component.  
[DestroyGameObjectHierarchy](ObjectChangeKind.DestroyGameObjectHierarchy.html)|
A change of this type indicates that a GameObject and the entire hierarchy
below it has been destroyed. This happens for example when
Undo.DestroyObjectImmediate is used with an GameObject.  
[CreateAssetObject](ObjectChangeKind.CreateAssetObject.html)| A change of this
type indicates that an asset object has been created. This happens for example
when Undo.RegisterCreatedObjectUndo is used with an instance of an asset (e.g.
Texture). Note that this only covers creation of asset objects in memory and
not creation of new assets in the project on disk.  
[DestroyAssetObject](ObjectChangeKind.DestroyAssetObject.html)| A change of
this type indicates that an asset object has been destroyed. This happens for
example when Undo.DestroyObjectImmediate is used with an instance of an asset
(e.g. Texture). Note that this only covers destruction of asset objects in
memory and not deletion of assets in the project on disk.  
[ChangeAssetObjectProperties](ObjectChangeKind.ChangeAssetObjectProperties.html)|
A change of this type indicates that a property of an asset object in memory
has changed. This happens for example when Undo.RecordObject is used with an
instance of an asset (e.g. Texture). Note that this only covers changes to
asset objects in memory and not changes to assets in the project on disk.  
[UpdatePrefabInstances](ObjectChangeKind.UpdatePrefabInstances.html)| A change
of this type indicates that prefab instances in an open scene have been
updated due to a change to the source prefab.  
[ChangeChildrenOrder](ObjectChangeKind.ChangeChildrenOrder.html)| A change of
this type indicates that a child has been reordered in the hierarchy under the
same parent. This happens when Undo.RegisterChildrenOrderUndo is called or
when reordering a child in the hierarchy under the same parent.  
[ChangeRootOrder](ObjectChangeKind.ChangeRootOrder.html)| A change of this
type indicates that a GameObject placed at the scene root has been reordered
in the hierarchy. This happens when Undo.SetSiblingIndex is called or when
reordering such a GameObject in the hierarchy under the same scene.  
  
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

