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

# ObjectChangeEventStream

struct in UnityEditor

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

Represents a stream of events that describes the changes applied to objects in
memory over the course of a frame.

### Properties

[isCreated](ObjectChangeEventStream-isCreated.html)| Indicates whether the
ObjectChangeEventStream has an allocated memory buffer.  
---|---  
[length](ObjectChangeEventStream-length.html)| The number of events in the
stream.  
  
### Public Methods

[Clone](ObjectChangeEventStream.Clone.html)| Creates a copy of this stream
with the specified allocator.  
---|---  
[Dispose](ObjectChangeEventStream.Dispose.html)| Releases the memory
associated with this stream.  
[GetChangeAssetObjectPropertiesEvent](ObjectChangeEventStream.GetChangeAssetObjectPropertiesEvent.html)|
Retrieves the event data at the given index as a
ChangeAssetObjectPropertiesEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
[GetChangeChildrenOrderEvent](ObjectChangeEventStream.GetChangeChildrenOrderEvent.html)|
Retrieves the event data at the given index as a ChangeChildrenOrderEventArgs.
Throws an exception if the event type requested does not match the event
stored in the stream.  
[GetChangeGameObjectOrComponentPropertiesEvent](ObjectChangeEventStream.GetChangeGameObjectOrComponentPropertiesEvent.html)|
Retrieves the event data at the given index as a
ChangeAssetObjectPropertiesEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
[GetChangeGameObjectParentEvent](ObjectChangeEventStream.GetChangeGameObjectParentEvent.html)|
Retrieves the event data at the given index as a
ChangeGameObjectParentEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
[GetChangeGameObjectStructureEvent](ObjectChangeEventStream.GetChangeGameObjectStructureEvent.html)|
Retrieves the event data at the given index as a
ChangeGameObjectStructureEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
[GetChangeGameObjectStructureHierarchyEvent](ObjectChangeEventStream.GetChangeGameObjectStructureHierarchyEvent.html)|
Retrieves the event data at the given index as a
ChangeGameObjectStructureHierarchyEventArgs. Throws an exception if the event
type requested does not match the event stored in the stream.  
[GetChangeRootOrderEvent](ObjectChangeEventStream.GetChangeRootOrderEvent.html)|
Retrieves the event data at the given index as a ChangeRootOrderEventArgs.
Throws an exception if the event type requested does not match the event
stored in the stream.  
[GetChangeSceneEvent](ObjectChangeEventStream.GetChangeSceneEvent.html)|
Retrieves the event data at the given index as a ChangeSceneEventArgs. Throws
an exception if the event type requested does not match the event stored in
the stream.  
[GetCreateAssetObjectEvent](ObjectChangeEventStream.GetCreateAssetObjectEvent.html)|
Retrieves the event data at the given index as a CreateAssetObjectEventArgs.
Throws an exception if the event type requested does not match the event
stored in the stream.  
[GetCreateGameObjectHierarchyEvent](ObjectChangeEventStream.GetCreateGameObjectHierarchyEvent.html)|
Retrieves the event data at the given index as a
CreateGameObjectHierarchyEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
[GetDestroyAssetObjectEvent](ObjectChangeEventStream.GetDestroyAssetObjectEvent.html)|
Retrieves the event data at the given index as a DestroyAssetObjectEventArgs.
Throws an exception if the event type requested does not match the event
stored in the stream.  
[GetDestroyGameObjectHierarchyEvent](ObjectChangeEventStream.GetDestroyGameObjectHierarchyEvent.html)|
Retrieves the event data at the given index as a
DestroyGameObjectHierarchyEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
[GetEventType](ObjectChangeEventStream.GetEventType.html)| Returns the type of
the event at the specified index.  
[GetUpdatePrefabInstancesEvent](ObjectChangeEventStream.GetUpdatePrefabInstancesEvent.html)|
Retrieves the event data at the given index as a
UpdatePrefabInstancesEventArgs. Throws an exception if the event type
requested does not match the event stored in the stream.  
  
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

