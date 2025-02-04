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

# Builder

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

Provides a way to construct an instance of
[ObjectChangeEventStream](ObjectChangeEventStream.html).

### Properties

[eventCount](ObjectChangeEventStream.Builder-eventCount.html)| The number of
events that have been recorded in this instance so far.  
---|---  
  
### Constructors

[ObjectChangeEventStream.Builder](ObjectChangeEventStream.Builder-ctor.html)|
Constructs a new instance.  
---|---  
  
### Public Methods

[Dispose](ObjectChangeEventStream.Builder.Dispose.html)| Releases the memory
associated with this instance.  
---|---  
[PushChangeAssetObjectPropertiesEvent](ObjectChangeEventStream.Builder.PushChangeAssetObjectPropertiesEvent.html)|
Adds an ChangeAssetObjectPropertiesEventArgs to the end of the stream.  
[PushChangeGameObjectOrComponentPropertiesEvent](ObjectChangeEventStream.Builder.PushChangeGameObjectOrComponentPropertiesEvent.html)|
Adds an ChangeGameObjectOrComponentPropertiesEventArgs to the end of the
stream.  
[PushChangeGameObjectParentEvent](ObjectChangeEventStream.Builder.PushChangeGameObjectParentEvent.html)|
Adds an ChangeGameObjectParentEventArgs to the end of the stream.  
[PushChangeGameObjectStructureEvent](ObjectChangeEventStream.Builder.PushChangeGameObjectStructureEvent.html)|
Adds an ChangeGameObjectStructureEventArgs to the end of the stream.  
[PushChangeGameObjectStructureHierarchyEvent](ObjectChangeEventStream.Builder.PushChangeGameObjectStructureHierarchyEvent.html)|
Adds an ChangeGameObjectStructureHierarchyEventArgs to the end of the stream.  
[PushChangeSceneEvent](ObjectChangeEventStream.Builder.PushChangeSceneEvent.html)|
Adds an ChangeSceneEventArgs to the end of the stream.  
[PushCreateAssetObjectEvent](ObjectChangeEventStream.Builder.PushCreateAssetObjectEvent.html)|
Adds an CreateAssetObjectEventArgs to the end of the stream.  
[PushCreateGameObjectHierarchyEvent](ObjectChangeEventStream.Builder.PushCreateGameObjectHierarchyEvent.html)|
Adds an CreateGameObjectHierarchyEventArgs to the end of the stream.  
[PushDestroyAssetObjectEvent](ObjectChangeEventStream.Builder.PushDestroyAssetObjectEvent.html)|
Adds an DestroyAssetObjectEventArgs to the end of the stream.  
[PushDestroyGameObjectHierarchyEvent](ObjectChangeEventStream.Builder.PushDestroyGameObjectHierarchyEvent.html)|
Adds an DestroyGameObjectHierarchyEventArgs to the end of the stream.  
[PushUpdatePrefabInstancesEvent](ObjectChangeEventStream.Builder.PushUpdatePrefabInstancesEvent.html)|
Adds an UpdatePrefabInstancesEventArgs to the end of the stream.  
[ToStream](ObjectChangeEventStream.Builder.ToStream.html)| Copies the data
collected in this instance into a new ObjectChangeEventStream instance.  
  
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

