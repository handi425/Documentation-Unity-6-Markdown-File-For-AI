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

# NavMeshAgent

class in UnityEngine.AI

/

Inherits from:[Behaviour](Behaviour.html)

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

Navigation mesh agent.

Attach this component to a mobile character in the game to allow the character
to use the NavMesh to navigate the scene. For more details refer to [AI
Navigation](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html).

### Properties

[acceleration](AI.NavMeshAgent-acceleration.html)| The maximum acceleration of
an agent as it follows a path, given in units / sec^2.  
---|---  
[agentTypeID](AI.NavMeshAgent-agentTypeID.html)| The type ID for the agent.  
[angularSpeed](AI.NavMeshAgent-angularSpeed.html)| Maximum turning speed in
(deg/s) while following a path.  
[areaMask](AI.NavMeshAgent-areaMask.html)| Specifies which NavMesh areas are
passable. Changing areaMask will make the path stale (see isPathStale).  
[autoBraking](AI.NavMeshAgent-autoBraking.html)| Should the agent brake
automatically to avoid overshooting the destination point?  
[autoRepath](AI.NavMeshAgent-autoRepath.html)| Should the agent attempt to
acquire a new path if the existing path becomes invalid?  
[autoTraverseOffMeshLink](AI.NavMeshAgent-autoTraverseOffMeshLink.html)|
Should the agent move across OffMeshLinks automatically?  
[avoidancePriority](AI.NavMeshAgent-avoidancePriority.html)| The avoidance
priority level.  
[baseOffset](AI.NavMeshAgent-baseOffset.html)| The relative vertical
displacement of the owning GameObject.  
[currentOffMeshLinkData](AI.NavMeshAgent-currentOffMeshLinkData.html)| The
current OffMeshLinkData.  
[desiredVelocity](AI.NavMeshAgent-desiredVelocity.html)| The desired velocity
of the agent including any potential contribution from avoidance. (Read Only)  
[destination](AI.NavMeshAgent-destination.html)| Gets or attempts to set the
destination of the agent in world-space units.  
[hasPath](AI.NavMeshAgent-hasPath.html)| Does the agent currently have a path?
(Read Only)  
[height](AI.NavMeshAgent-height.html)| The height of the agent for purposes of
passing under obstacles, etc.  
[isOnNavMesh](AI.NavMeshAgent-isOnNavMesh.html)| Is the agent currently bound
to the navmesh? (Read Only)  
[isOnOffMeshLink](AI.NavMeshAgent-isOnOffMeshLink.html)| Is the agent
currently positioned on an OffMeshLink? (Read Only)  
[isPathStale](AI.NavMeshAgent-isPathStale.html)| Is the current path stale.
(Read Only)  
[isStopped](AI.NavMeshAgent-isStopped.html)| Use this property to set, or get,
whether the NavMesh agent stops or continues its movement along the current
path.  
[navMeshOwner](AI.NavMeshAgent-navMeshOwner.html)| Returns the owning object
of the NavMesh the agent is currently placed on (Read Only).  
[nextOffMeshLinkData](AI.NavMeshAgent-nextOffMeshLinkData.html)| The next
OffMeshLinkData on the current path.  
[nextPosition](AI.NavMeshAgent-nextPosition.html)| Gets or sets the simulation
position of the navmesh agent.  
[obstacleAvoidanceType](AI.NavMeshAgent-obstacleAvoidanceType.html)| The level
of quality of avoidance.  
[path](AI.NavMeshAgent-path.html)| Property to get and set the current path.  
[pathPending](AI.NavMeshAgent-pathPending.html)| Is a path in the process of
being computed but not yet ready? (Read Only)  
[pathStatus](AI.NavMeshAgent-pathStatus.html)| The status of the current path
(complete, partial or invalid).  
[radius](AI.NavMeshAgent-radius.html)| The avoidance radius for the agent.  
[remainingDistance](AI.NavMeshAgent-remainingDistance.html)| The distance
between the agent's position and the destination on the current path. (Read
Only)  
[speed](AI.NavMeshAgent-speed.html)| Maximum movement speed when following a
path.  
[steeringTarget](AI.NavMeshAgent-steeringTarget.html)| Get the current
steering target along the path. (Read Only)  
[stoppingDistance](AI.NavMeshAgent-stoppingDistance.html)| Stop within this
distance from the target position.  
[updatePosition](AI.NavMeshAgent-updatePosition.html)| Gets or sets whether
the transform position is synchronized with the simulated agent position. The
default value is true.  
[updateRotation](AI.NavMeshAgent-updateRotation.html)| Should the agent update
the transform orientation?  
[updateUpAxis](AI.NavMeshAgent-updateUpAxis.html)| Allows you to specify
whether the agent should be aligned to the up-axis of the NavMesh or link that
it is placed on.  
[velocity](AI.NavMeshAgent-velocity.html)| Access the current velocity of the
NavMeshAgent component, or set a velocity to control the agent manually.  
  
### Public Methods

[ActivateCurrentOffMeshLink](AI.NavMeshAgent.ActivateCurrentOffMeshLink.html)|
Enables or disables the current off-mesh link.  
---|---  
[CalculatePath](AI.NavMeshAgent.CalculatePath.html)| Calculate a path to a
specified point and store the resulting path.  
[CompleteOffMeshLink](AI.NavMeshAgent.CompleteOffMeshLink.html)| Completes the
movement on the current OffMeshLink.  
[FindClosestEdge](AI.NavMeshAgent.FindClosestEdge.html)| Locate the closest
NavMesh edge.  
[GetAreaCost](AI.NavMeshAgent.GetAreaCost.html)| Gets the cost for path
calculation when crossing area of a particular type.  
[Move](AI.NavMeshAgent.Move.html)| Apply relative movement to current
position.  
[Raycast](AI.NavMeshAgent.Raycast.html)| Trace a straight path towards a
target postion in the NavMesh without moving the agent.  
[ResetPath](AI.NavMeshAgent.ResetPath.html)| Clears the current path.  
[SamplePathPosition](AI.NavMeshAgent.SamplePathPosition.html)| Sample a
position along the current path.  
[SetAreaCost](AI.NavMeshAgent.SetAreaCost.html)| Sets the cost for traversing
over areas of the area type.  
[SetDestination](AI.NavMeshAgent.SetDestination.html)| Sets or updates the
destination thus triggering the calculation for a new path.  
[SetPath](AI.NavMeshAgent.SetPath.html)| Assign a new path to this agent.  
[Warp](AI.NavMeshAgent.Warp.html)| Warps agent to the provided position.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

