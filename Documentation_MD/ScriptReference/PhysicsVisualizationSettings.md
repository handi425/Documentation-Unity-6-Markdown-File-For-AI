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

# PhysicsVisualizationSettings

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

This class contains the settings controlling the Physics Debug Visualization.

Additional resources: [PhysicsDebugWindow](PhysicsDebugWindow.html).

### Static Properties

[articulationBodyColor](PhysicsVisualizationSettings-
articulationBodyColor.html)| Color for Articulation Bodies.  
---|---  
[baseAlpha](PhysicsVisualizationSettings-baseAlpha.html)| Alpha amount used
for transparency blending.  
[centerOfMassUseScreenSize](PhysicsVisualizationSettings-
centerOfMassUseScreenSize.html)| Whether or not the center of mass
visualization should be constant screen space size.  
[colorVariance](PhysicsVisualizationSettings-colorVariance.html)| Used to
disinguish neighboring Colliders.  
[contactColor](PhysicsVisualizationSettings-contactColor.html)| Contact arrow
color.  
[contactImpulseColor](PhysicsVisualizationSettings-contactImpulseColor.html)|
ContactPoint.impulse arrow color.  
[contactSeparationColor](PhysicsVisualizationSettings-
contactSeparationColor.html)| Contact point separation color.  
[devOptions](PhysicsVisualizationSettings-devOptions.html)| Shows extra
options used to develop and debug the physics visualization.  
[dirtyCount](PhysicsVisualizationSettings-dirtyCount.html)| Dirty marker used
for refreshing the GUI.  
[enableMouseSelect](PhysicsVisualizationSettings-enableMouseSelect.html)|
Enables the mouse-over highlighting and mouse selection modes.  
[forceOverdraw](PhysicsVisualizationSettings-forceOverdraw.html)| Forcing the
drawing of Colliders on top of any other geometry, regardless of depth.  
[inertiaTensorScale](PhysicsVisualizationSettings-inertiaTensorScale.html)|
The scale by which the inertia tensor lines are multiplied.  
[kinematicColor](PhysicsVisualizationSettings-kinematicColor.html)| Color for
kinematic Rigidbodies.  
[maxNumberOfQueries](PhysicsVisualizationSettings-maxNumberOfQueries.html)|
The maximum number of queries that the PhysicsDebugWindow will visualize at
one given time.  
[queryColor](PhysicsVisualizationSettings-queryColor.html)| Color that the
Physics Debugger uses for query visualization.  
[rigidbodyColor](PhysicsVisualizationSettings-rigidbodyColor.html)| Color for
Rigidbodies, primarily active ones.  
[showAllContacts](PhysicsVisualizationSettings-showAllContacts.html)| Whether
the PhysicsDebugWindow visualizes all contacts.  
[showCollisionGeometry](PhysicsVisualizationSettings-
showCollisionGeometry.html)| Should the PhysicsDebugWindow display the
collision geometry.  
[showContactImpulse](PhysicsVisualizationSettings-showContactImpulse.html)|
Whether the PhysicsDebugWindow shows ContactPoint.impulse.  
[showContacts](PhysicsVisualizationSettings-showContacts.html)| Whether the
PhysicsDebugWindow shows contacts.  
[showContactSeparation](PhysicsVisualizationSettings-
showContactSeparation.html)| Whether the PhysicsDebugWindow shows contact
separation.  
[sleepingBodyColor](PhysicsVisualizationSettings-sleepingBodyColor.html)|
Color for Rigidbodies that are controlled by the physics simulator, but are
not currently being simulated.  
[staticColor](PhysicsVisualizationSettings-staticColor.html)| Color for
Colliders that do not have a Rigidbody component.  
[terrainTilesMax](PhysicsVisualizationSettings-terrainTilesMax.html)| Maximum
number of mesh tiles available to draw all Terrain Colliders.  
[triggerColor](PhysicsVisualizationSettings-triggerColor.html)| Color for
Colliders that are Triggers.  
[useContactFiltering](PhysicsVisualizationSettings-useContactFiltering.html)|
Whether PhysicsDebugWindow takes the PhysicsVisualizationSettings filtering
settings into account when visualizing contacts.  
[useSceneCam](PhysicsVisualizationSettings-useSceneCam.html)| Controls whether
the SceneView or the GameView camera is used. Not shown in the UI.  
[useVariedContactColors](PhysicsVisualizationSettings-
useVariedContactColors.html)| Whether varied colors are used for
PhysicsDebugWindow contact visualization.  
[viewDistance](PhysicsVisualizationSettings-viewDistance.html)| Colliders
within this distance will be displayed.  
  
### Static Methods

[ClearMouseHighlight](PhysicsVisualizationSettings.ClearMouseHighlight.html)|
Clears the highlighted Collider.  
---|---  
[DeinitDebugDraw](PhysicsVisualizationSettings.DeinitDebugDraw.html)|
Deinitializes the physics debug visualization system and tracking of changes
Colliders.  
[GetQueryFilterState](PhysicsVisualizationSettings.GetQueryFilterState.html)|
Gets the query filtering state of PhysicsVisualizationSettings  
[GetShowArticulationBodies](PhysicsVisualizationSettings.GetShowArticulationBodies.html)|
Should Articulation Bodies be shown by the Physics Visualizer.  
[GetShowBoxColliders](PhysicsVisualizationSettings.GetShowBoxColliders.html)|
Should BoxColliders be shown.  
[GetShowCapsuleColliders](PhysicsVisualizationSettings.GetShowCapsuleColliders.html)|
Should CapsuleColliders be shown.  
[GetShowCollisionLayer](PhysicsVisualizationSettings.GetShowCollisionLayer.html)|
Should the given layer be considered by the display filter.  
[GetShowCollisionLayerMask](PhysicsVisualizationSettings.GetShowCollisionLayerMask.html)|
Should the mask representing the layers be considered by the display filter.  
[GetShowKinematicBodies](PhysicsVisualizationSettings.GetShowKinematicBodies.html)|
Should the kinematic Rigidbodies be considered by the display filter.  
[GetShowMeshColliders](PhysicsVisualizationSettings.GetShowMeshColliders.html)|
Should MeshColliders be shown.  
[GetShowPhysicsSceneMask](PhysicsVisualizationSettings.GetShowPhysicsSceneMask.html)|
Return a mask representing scenes that are enabled by display filter  
[GetShowRigidbodies](PhysicsVisualizationSettings.GetShowRigidbodies.html)|
Should any Rigidbodies be considered by the display filter.  
[GetShowSleepingBodies](PhysicsVisualizationSettings.GetShowSleepingBodies.html)|
Should the sleeping Rigidbodies be considered by the display filter.  
[GetShowSphereColliders](PhysicsVisualizationSettings.GetShowSphereColliders.html)|
Should SphereColliders be shown.  
[GetShowStaticColliders](PhysicsVisualizationSettings.GetShowStaticColliders.html)|
Should the Colliders without a Rigidbody component be considered by the
display filter.  
[GetShowTerrainColliders](PhysicsVisualizationSettings.GetShowTerrainColliders.html)|
Should TerrainColliders be shown.  
[GetShowTriggers](PhysicsVisualizationSettings.GetShowTriggers.html)| Should
the triggers be considered by the display filter.  
[GetShowUnitySceneMask](PhysicsVisualizationSettings.GetShowUnitySceneMask.html)|
Returns a mask that represents Unity scenes that are enabled by the display
filter.  
[HasMouseHighlight](PhysicsVisualizationSettings.HasMouseHighlight.html)|
Returns true if there currently is any kind of physics object highlighted.  
[InitDebugDraw](PhysicsVisualizationSettings.InitDebugDraw.html)| Initializes
the physics debug visualization system. The system must be initialized for any
physics objects to be visualized. It is normally initialized by the
PhysicsDebugWindow.  
[Reset](PhysicsVisualizationSettings.Reset.html)| Resets the visualization
options to their default state.  
[SetQueryFilterState](PhysicsVisualizationSettings.SetQueryFilterState.html)|
Sets the query filtering state of PhysicsVisualizationSettings  
[SetShowArticulationBodies](PhysicsVisualizationSettings.SetShowArticulationBodies.html)|
Should Articulation Bodies be shown by the Physics Visualizer.  
[SetShowBoxColliders](PhysicsVisualizationSettings.SetShowBoxColliders.html)|
Should BoxColliders be shown.  
[SetShowCapsuleColliders](PhysicsVisualizationSettings.SetShowCapsuleColliders.html)|
Should CapsuleColliders be shown.  
[SetShowCollisionLayer](PhysicsVisualizationSettings.SetShowCollisionLayer.html)|
Should the given layer be considered by the display filter.  
[SetShowCollisionLayerMask](PhysicsVisualizationSettings.SetShowCollisionLayerMask.html)|
Should the mask representing the layers be considered by the display filter.  
[SetShowForAllFilters](PhysicsVisualizationSettings.SetShowForAllFilters.html)|
Enables or disables all filtering items.  
[SetShowKinematicBodies](PhysicsVisualizationSettings.SetShowKinematicBodies.html)|
Should the kinematic Rigidbodies be considered by the display filter.  
[SetShowMeshColliders](PhysicsVisualizationSettings.SetShowMeshColliders.html)|
Should MeshColliders be shown.  
[SetShowPhysicsSceneMask](PhysicsVisualizationSettings.SetShowPhysicsSceneMask.html)|
Should the scene mask be considered by the display filter.  
[SetShowRigidbodies](PhysicsVisualizationSettings.SetShowRigidbodies.html)|
Should any Rigidbodies be considered by the display filter.  
[SetShowSleepingBodies](PhysicsVisualizationSettings.SetShowSleepingBodies.html)|
Should sleeping Rigidbodies and Articulation Bodies be considered by the
display filter.  
[SetShowSphereColliders](PhysicsVisualizationSettings.SetShowSphereColliders.html)|
Should SphereColliders be shown.  
[SetShowStaticColliders](PhysicsVisualizationSettings.SetShowStaticColliders.html)|
Should the Colliders without a Rigidbody component be considered by the
display filter.  
[SetShowTerrainColliders](PhysicsVisualizationSettings.SetShowTerrainColliders.html)|
Should TerrainColliders be shown.  
[SetShowTriggers](PhysicsVisualizationSettings.SetShowTriggers.html)| Should
the triggers be considered by the display filter.  
[SetShowUnitySceneMask](PhysicsVisualizationSettings.SetShowUnitySceneMask.html)|
Sets the Unity scene mask that should be considered by the filter.  
[UpdateMouseHighlight](PhysicsVisualizationSettings.UpdateMouseHighlight.html)|
Updates the mouse-over highlight at the given mouse position in screen space.  
  
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

