[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CullingGroupAPI-getstarted.html)
  * [中文](/cn/current/Manual/CullingGroupAPI-getstarted.html)
  * [日本語](/ja/current/Manual/CullingGroupAPI-getstarted.html)
  * [한국어](/kr/current/Manual/CullingGroupAPI-getstarted.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CullingGroupAPI-getstarted.html)
  * [中文](/cn/current/Manual/CullingGroupAPI-getstarted.html)
  * [日本語](/ja/current/Manual/CullingGroupAPI-getstarted.html)
  * [한국어](/kr/current/Manual/CullingGroupAPI-getstarted.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
  * [Configure culling with the CullingGroup API](CullingGroupAPI-landing.html)
  * Create a Culling Group

[](CullingGroupAPI.html)

Introduction to the CullingGroup API

[](CullingGroupAPI-get-culling-results.html)

Get culling results

# Create a Culling Group

There are no components or visual tools for working with CullingGroups; they
are purely accessible via script.

A CullingGroup can be constructed using the ‘new’ operator:

    
    
    CullingGroup group = new CullingGroup();
    

To have the CullingGroup perform visibility and/or distance calculations,
specify the **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) it should use:

    
    
    group.targetCamera = Camera.main;
    

Create and populate an array of BoundingSphere structures with the positions
and radii of your spheres, and pass it to SetBoundingSpheres along with the
number of spheres that are actually in the array. The number of spheres does
not need to be the same as the length of the array. Unity recommends that you
create an array that is big enough to hold the most spheres you will ever have
at one time, even if the initial number of spheres you actually have in the
array is very low. Using a larger array allows you to add or remove spheres as
needed without the computationally expensive process of resizing the array at
runtime.

    
    
    BoundingSphere[] spheres = new BoundingSphere[1000];
    spheres[0] = new BoundingSphere(Vector3.zero, 1f);
    group.SetBoundingSpheres(spheres);
    group.SetBoundingSphereCount(1);
    

At this point, the CullingGroup will begin computing the visibility of the
single sphere each frame.

To clean up the CullingGroup and free all memory it uses, dispose of the
CullingGroup via the standard .NET IDisposable mechanism:

    
    
    group.Dispose();
    group = null;
    

[](CullingGroupAPI.html)

Introduction to the CullingGroup API

[](CullingGroupAPI-get-culling-results.html)

Get culling results

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

