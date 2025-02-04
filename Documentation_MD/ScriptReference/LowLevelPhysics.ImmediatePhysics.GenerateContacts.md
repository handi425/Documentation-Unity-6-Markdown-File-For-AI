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

#  [ImmediatePhysics](LowLevelPhysics.ImmediatePhysics.html).GenerateContacts

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

public static int GenerateContacts(ReadOnly<GeometryHolder> geom1,
ReadOnly<GeometryHolder> geom2, ReadOnly<ImmediateTransform> xform1,
ReadOnly<ImmediateTransform> xform2, int pairCount,
NativeArray<ImmediateContact> outContacts, NativeArray<int> outContactCounts,
float contactDistance);

### Parameters

geom1 | The array that holds the first member of each pair of [GeometryHolder](LowLevelPhysics.GeometryHolder.html) objects with shapes assigned.  
---|---  
geom2 | The array that holds the second member of each pair of [GeometryHolder](LowLevelPhysics.GeometryHolder.html) objects with shapes assigned.  
xform1 | The array that holds the first member of each pair of [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)s.  
xform2 | The array that holds the second member of each pair of [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)s.  
pairCount | The number of pairs provided in the [GeometryHolder](LowLevelPhysics.GeometryHolder.html) and [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html) arrays.  
outContacts | The output array of contacts that were generated.  
outContactCounts | The output array of how many contacts were generated for each pair.  
contactDistance | The distance at which contacts begin to be generated between the pairs.  
  
### Returns

**int** Returns the total number of contact points that were generated.

### Description

Generates the contact points for all the given pairs of shapes. Stores the
resulting contacts in the
[ImmediateContact](LowLevelPhysics.ImmediateContact.html) array, and the
number of contacts per each pair in the `outContactCounts` array.

This code sample defines how many pairs of objects PhysX should expect in the
scene. You can set a specific number for a small contact check or, if you
intend to run a more complex simulation, you might want to implement
broadphase filtering to find out how many pairs of objects will interact. The
easiest and least performant option is to put all the possible pairs of bodies
into a GenerateContacts function that exists in the scene. This example shows
a basic setup of manually adding two pairs of bodies and checking for contacts
between them.

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.LowLevelPhysics;
    using Unity.Collections;  
      
    public class ImmediatePhysics_GenerateContacts_Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private int m_NumberOfPairs = 2;  
      
        // Pull in a reference from the [Editor](Editor.html) to the [Mesh](Mesh.html) [Collider](Collider.html).
        [[SerializeField](SerializeField.html)]
        private [MeshCollider](MeshCollider.html) m_Mesh;  
      
        List<[Vector3](Vector3.html)> contactPoints = new List<[Vector3](Vector3.html)>();  
      
        // There is no way to know how many contacts the shapes will generate,
        // so set a maximum value that should confidently fit all of them.
        int s_MaxContactCount = 100;  
      
        void Start()
        {
            // Create and set up geometry and transform arrays.
            NativeArray<[GeometryHolder](LowLevelPhysics.GeometryHolder.html)> geom1 = new NativeArray<[GeometryHolder](LowLevelPhysics.GeometryHolder.html)>(m_NumberOfPairs, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            NativeArray<[GeometryHolder](LowLevelPhysics.GeometryHolder.html)> geom2 = new NativeArray<[GeometryHolder](LowLevelPhysics.GeometryHolder.html)>(m_NumberOfPairs, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));  
      
            // Create a box shape that is 1 meter wide on each axis, and use that to construct a [GeometryHolder](LowLevelPhysics.GeometryHolder.html) object.
            [BoxGeometry](LowLevelPhysics.BoxGeometry.html) boxShape = new [BoxGeometry](LowLevelPhysics.BoxGeometry.html)(new [Vector3](Vector3.html)(0.5f, 0.5f, 0.5f));
            [GeometryHolder](LowLevelPhysics.GeometryHolder.html) box = [GeometryHolder.Create](LowLevelPhysics.GeometryHolder.Create.html)(boxShape);  
      
            // Get the geometry of an existing collider.
            [GeometryHolder](LowLevelPhysics.GeometryHolder.html) convexMesh = m_Mesh.GeometryHolder;  
      
            NativeArray<[ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)> xForms1 = new NativeArray<[ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)>(m_NumberOfPairs, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            NativeArray<[ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)> xForms2 = new NativeArray<[ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)>(m_NumberOfPairs, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));  
      
            [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html) body1Transform = new [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)
            {
                [Position](UIElements.Position.html) = new [Vector3](Vector3.html)(0, 0, 0),
                Rotation = [Quaternion.identity](Quaternion-identity.html)
            };  
      
            [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html) body2Transform = new [ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)
            {
                [Position](UIElements.Position.html) = new [Vector3](Vector3.html)(0, 0.75f, 0),
                Rotation = [Quaternion.Euler](Quaternion.Euler.html)(new [Vector3](Vector3.html)(45f, 0, 0))
            };  
      
    
            // First pair is two boxes interacting.
            geom1[0] = box;
            geom2[0] = box;  
      
            xForms1[0] = body1Transform;
            xForms2[0] = body2Transform;  
      
            // Second pair is a box and a convex [Mesh](Mesh.html) [Collider](Collider.html).
            geom1[1] = convexMesh;
            geom1[2] = box;  
      
            xForms1[1] = body1Transform;
            xForms2[1] = body2Transform;  
      
            // This code re-uses the same transforms, which means that if all the bodies
            // were part of the same simulation, they would all overlap with each other. However,
            // because we are only generating contacts per pair, one pair of bodies does not affect
            // the other pairs.  
      
            // Create a place to hold the output contacts and their counts per pair.
            // There is no way to know how many contacts the shapes will generate,
            // so set a maximum value that should confidently fit all of them.
            NativeArray<[ImmediateContact](LowLevelPhysics.ImmediateContact.html)> contacts = new NativeArray<[ImmediateContact](LowLevelPhysics.ImmediateContact.html)>(s_MaxContactCount, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            // The number of contactCounts is the same as the number of pairs.
            NativeArray<int> contactCounts = new NativeArray<int>(m_NumberOfPairs, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));  
      
            // Finally, call the GenerateContacts function and put all the arrays in. 
            // Keep note of the [ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html) status of the input arrays.  
      
            var totalContacts = [ImmediatePhysics.GenerateContacts](LowLevelPhysics.ImmediatePhysics.GenerateContacts.html)(geom1.AsReadOnly(), geom2.AsReadOnly(), xForms1.AsReadOnly(), xForms2.AsReadOnly(), m_NumberOfPairs, contacts, contactCounts);  
      
            // It is now possible to check whether there were any contacts for the pairs.
            // First, iterate over the number of input pairs defined in m_NumberOfPairs.
            int idx = 0;
            for (int i = 0; i < m_NumberOfPairs; i++)
            {
                // Iterate over the number of contacts that were generated per each pair.
                for (int j = 0; j < contactCounts[i]; j++)
                {
                    // Add the contact points to a list for visualization later.
                    contactPoints.Add(contacts[idx].Point);  
      
                    // The number of contact points per each pair can be variable, so
                    // use a separate index to keep track of which contact to retrieve.
                    idx++;
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

