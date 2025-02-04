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

#  [ObjectChangeEvents](ObjectChangeEvents.html).changesPublished

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

### Parameters

value | The stream of events that have been recorded since the last frame.  
---|---  
  
### Description

Event that is raised once per frame if any undoable changes have been
recorded.

All undoable changes to any loaded object are recorded in a stream of events
and published once per frame. Subscribe to this event to react to any of these
changes. The changes appear in the stream in the order that they were applied.
Events in the stream do not necessarily map one-to-one to user interactions
since user interactions may consist of multiple changes. Note that the stream
passed to your callback is a temporary object owned by the engine. Do not
Dispose it. Make a copy if you intend to retain it for longer than the
duration of your callback.

    
    
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

