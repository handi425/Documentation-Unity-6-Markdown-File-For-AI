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

# NavMesh

class in UnityEngine.AI

/

Implemented in:[UnityEngine.AIModule](UnityEngine.AIModule.html)

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

Singleton class to access the baked NavMesh.

Use the NavMesh class to perform spatial queries such as pathfinding and
walkability tests. This class also lets you set the pathfinding cost for
specific area types, and tweak the global behavior of pathfinding and
avoidance.  
  
Before you can use spatial queries, you must first bake the NavMesh to your
scene.  
  
See also:  
• [Create a
NavMesh](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/CreateNavMesh.html)
– for more information on how to setup and bake NavMesh  
• [Areas and
Costs](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/AreasAndCosts.html)
– to learn how to use different Area types.  
• [NavMeshAgent](AI.NavMeshAgent.html) – to learn how to control and move
NavMesh Agents.  
• [NavMeshObstacle](AI.NavMeshObstacle.html) – to learn how to control NavMesh
Obstacles using scripting.  
•
[NavMeshLink](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/api/Unity.AI.Navigation.NavMeshLink.html)
– to learn how to control Off-Mesh Links using scripting.  

### Static Properties

[AllAreas](AI.NavMesh.AllAreas.html)| Area mask constant that includes all
NavMesh areas.  
---|---  
[avoidancePredictionTime](AI.NavMesh-avoidancePredictionTime.html)| Describes
how far in the future the agents predict collisions for avoidance.  
[onPreUpdate](AI.NavMesh-onPreUpdate.html)| Set a function to be called before
the NavMesh is updated during the frame update execution.  
[pathfindingIterationsPerFrame](AI.NavMesh-
pathfindingIterationsPerFrame.html)| The maximum number of nodes processed for
each frame during the asynchronous pathfinding process.  
  
### Static Methods

[AddLink](AI.NavMesh.AddLink.html)| Adds a link to the NavMesh. The link is
described by the NavMeshLinkData struct.  
---|---  
[AddNavMeshData](AI.NavMesh.AddNavMeshData.html)| Adds the specified
NavMeshData to the game.  
[CalculatePath](AI.NavMesh.CalculatePath.html)| Calculate a path between two
points and store the resulting path.  
[CalculateTriangulation](AI.NavMesh.CalculateTriangulation.html)| Calculates
triangulation of the current navmesh.  
[CreateSettings](AI.NavMesh.CreateSettings.html)| Creates and returns a new
entry of NavMesh build settings available for runtime NavMesh building.  
[FindClosestEdge](AI.NavMesh.FindClosestEdge.html)| Locate the closest NavMesh
edge from a point on the NavMesh.  
[GetAreaCost](AI.NavMesh.GetAreaCost.html)| Gets the cost for path finding
over geometry of the area type.  
[GetAreaFromName](AI.NavMesh.GetAreaFromName.html)| Returns the area index for
a named NavMesh area type.  
[GetAreaNames](AI.NavMesh.GetAreaNames.html)| Get all the NavMesh area names.  
[GetLinkOwner](AI.NavMesh.GetLinkOwner.html)| Gets the object, if any, that is
associated with the link instance.  
[GetSettingsByID](AI.NavMesh.GetSettingsByID.html)| Returns an existing entry
of NavMesh build settings.  
[GetSettingsByIndex](AI.NavMesh.GetSettingsByIndex.html)| Returns an existing
entry of NavMesh build settings by its ordered index.  
[GetSettingsCount](AI.NavMesh.GetSettingsCount.html)| Returns the number of
registered NavMesh build settings.  
[GetSettingsNameFromID](AI.NavMesh.GetSettingsNameFromID.html)| Returns the
name associated with the NavMesh build settings matching the provided agent
type ID.  
[IsLinkActive](AI.NavMesh.IsLinkActive.html)| Determines whether the instance
of the link can be used to calculate paths, and if NavMesh agents can move
over it.  
[IsLinkOccupied](AI.NavMesh.IsLinkOccupied.html)| Determines whether or not a
NavMesh agent is currently using this link.  
[IsLinkValid](AI.NavMesh.IsLinkValid.html)| Determines whether the link
instance is part of the current data used for navigation.  
[Raycast](AI.NavMesh.Raycast.html)| Trace a line between two points on the
NavMesh.  
[RemoveAllNavMeshData](AI.NavMesh.RemoveAllNavMeshData.html)| Removes all
NavMesh surfaces and links from the game.  
[RemoveLink](AI.NavMesh.RemoveLink.html)| Removes a link from the NavMesh.  
[RemoveNavMeshData](AI.NavMesh.RemoveNavMeshData.html)| Removes the specified
NavMeshDataInstance from the game, making it unavailable for agents and
queries.  
[RemoveSettings](AI.NavMesh.RemoveSettings.html)| Removes the build settings
matching the agent type ID.  
[SamplePosition](AI.NavMesh.SamplePosition.html)| Finds the nearest point
based on the NavMesh within a specified range.  
[SetAreaCost](AI.NavMesh.SetAreaCost.html)| Sets the cost for finding path
over geometry of the area type on all agents.  
[SetLinkActive](AI.NavMesh.SetLinkActive.html)| Activates or deactivates the
link instance. An active link instance can be traversed by agents and used to
plan paths, but a deactivated link cannot.  
[SetLinkOwner](AI.NavMesh.SetLinkOwner.html)| Associates an object with the
instance of a link.  
  
### Delegates

[OnNavMeshPreUpdate](AI.NavMesh.OnNavMeshPreUpdate.html)| Registers callback
methods to be invoked before the NavMesh system updates.  
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

