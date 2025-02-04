[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-optimizing-arrays.html)
  * [中文](/cn/current/Manual/performance-optimizing-arrays.html)
  * [日本語](/ja/current/Manual/performance-optimizing-arrays.html)
  * [한국어](/kr/current/Manual/performance-optimizing-arrays.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-optimizing-arrays.html)
  * [中文](/cn/current/Manual/performance-optimizing-arrays.html)
  * [日本語](/ja/current/Manual/performance-optimizing-arrays.html)
  * [한국어](/kr/current/Manual/performance-optimizing-arrays.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Managed memory](performance-managed-memory.html)
  * [Optimizing your code for managed memory](performance-optimizing-code-managed-memory.html)
  * Optimizing arrays

[](performance-reusable-code.html)

Using coding patterns with reusable memory

[](performance-native-memory.html)

Native memory

# Optimizing arrays

The following page outlines examples to improve the performance of your code
when using [arrays](https://learn.microsoft.com/en-us/dotnet/csharp/language-
reference/builtin-types/arrays).

## Pass arrays as parameters to methods

Sometimes it might be convenient to write a method that creates a new array,
fills the array with values and then returns it. However, if this method is
called repeatedly, then new memory gets allocated each time.

The following example code shows an example of a method which creates an array
every time it’s called:

    
    
    // Bad C# script example: Every time the RandomList method is called it
    // allocates a new array
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        float[] RandomList(int numElements) {
            var result = new float[numElements];
            
            for (int i = 0; i < numElements; i++) {
                result[i] = Random.value;
            }
            
            return result;
        }
    }
    

One way you can avoid allocating memory every time is to make use of the fact
that an array is a reference type. You can modify an array that’s passed into
a method as a parameter, and the results remain after the method returns. To
do this, you can configure the example code as follows:

    
    
    // Good C# script example: This version of method is passed an array to fill
    // with random values. The array can be cached and re-used to avoid repeated
    // temporary allocations
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        void RandomList(float[] arrayToFill) {
            for (int i = 0; i < arrayToFill.Length; i++) {
                arrayToFill[i] = Random.value;
            }
        }
    }
    

This code replaces the existing contents of the array with new values. This
workflow requires the calling code to do the initial allocation of the array,
but the function doesn’t generate any new garbage when it’s called. The array
can then be re-used and re-filled with random numbers the next time this
method is called without any new allocations on the managed heap.

## Avoid repeated access to array-valued Unity APIs

One cause of unintended allocations on arrays is the repeated accessing of
Unity APIs that return arrays. All Unity APIs that return arrays create a new
copy of the array each time they’re accessed. If your code accesses an array-
valued Unity API more often than necessary, it can affect the performance of
your application.

As an example, the following code creates four copies of the vertices array
per loop iteration. The allocations happen each time the `.vertices` property
is accessed:

    
    
    // Bad C# script example: this loop create 4 copies of the vertices array per iteration
    void Update() {
        for(int i = 0; i < mesh.vertices.Length; i++) {
            float x, y, z;
    
            x = mesh.vertices[i].x;
            y = mesh.vertices[i].y;
            z = mesh.vertices[i].z;
    
            // ...
    
            DoSomething(x, y, z);   
        }
    }
    
    

You can refactor this code into a single array allocation, regardless of the
number of loop iterations. To do this, configure your code to capture the
vertices array before the loop:

    
    
    // Better C# script example: create one copy of the vertices array
    // and work with that
    void Update() {
        var vertices = mesh.vertices;
    
        for(int i = 0; i < vertices.Length; i++) {
    
            float x, y, z;
    
            x = vertices[i].x;
            y = vertices[i].y;
            z = vertices[i].z;
    
            // ...
    
            DoSomething(x, y, z);   
        }
    }
    

An optimal way of doing this is to maintain a `List` of vertices which is
cached and re-used between frames, and then use
[`Mesh.GetVertices`](../ScriptReference/Mesh.GetVertices.html) to populate it
when required.

    
    
    // Best C# script example: create one copy of the vertices array
    // and work with that.
    List<Vector3> m_vertices = new List<Vector3>();
    
    void Update() {
        mesh.GetVertices(m_vertices);
    
        for(int i = 0; i < m_vertices.Length; i++) {
    
            float x, y, z;
    
            x = m_vertices[i].x;
            y = m_vertices[i].y;
            z = m_vertices[i].z;
    
            // ...
    
            DoSomething(x, y, z);   
        }
    }
    

While the CPU performance implications of accessing a property that allocates
an array once isn’t high, repeated accesses within tight loops create CPU
performance hotspots. Repeated accesses expand the [managed heap](performance-
managed-memory-introduction.html).

This problem is common on mobile devices, because the
[`Input.touches`](../ScriptReference/Input-touches.html) API behaves similarly
to the previous example. It’s also common for projects to contain code similar
to the following, where an allocation occurs each time the `.touches` property
is accessed:

    
    
    // Bad C# script example: Input.touches returns an array every time it’s accessed
    for ( int i = 0; i < Input.touches.Length; i++ ) {
       Touch touch = Input.touches[i];
    
        // …
    }
    

To improve this, you can configure your code to hoist the array allocation out
of the loop condition:

    
    
    // Better C# script example: Input.touches is only accessed once here
    Touch[] touches = Input.touches;
    
    for ( int i = 0; i < touches.Length; i++ ) {
    
       Touch touch = touches[i];
    
       // …
    }
    

The following code example converts the previous example to the allocation-
free `Touch` API:

    
    
    // BEST C# script example: Input.touchCount and Input.GetTouch don’t allocate at all.
    int touchCount = Input.touchCount;
    
    for ( int i = 0; i < touchCount; i++ ) {
       Touch touch = Input.GetTouch(i);
    
       // …
    }
    

**Note:** The property access (`Input.touchCount`) remains outside the loop
condition, to save the CPU impact of invoking the property’s get method.

### Alternative non-allocating APIs

Some Unity APIs have alternative versions that don’t cause memory allocations.
You should use these when possible. The following table contains an example of
allocating APIs and their non-allocating alternatives:

**Allocating API** | **Non-allocating API alternative**  
---|---  
[`Physics.RaycastAll`](../ScriptReference/Physics.RaycastAll.html) | [`Physics.RaycastNonAlloc`](../ScriptReference/Physics.RaycastNonAlloc.html)  
[`Animator.parameters`](../ScriptReference/Animator-parameters.html) |  [`Animator.parameterCount`](../ScriptReference/Animator-parameterCount.html) and [`Animator.GetParameter`](../ScriptReference/Animator.GetParameter.html)  
[`Renderer.sharedMaterials`](../ScriptReference/Renderer-sharedMaterials.html) | [`Renderer.GetSharedMaterials`](../ScriptReference/Renderer.GetSharedMaterials.html)  
  
In general, if the method returns an array, there’s usually a non-allocating
version of the API which you can use to pass the array to.

## Use static instances of zero-length arrays

Some development teams prefer to return empty arrays instead of `null` when an
array-valued method needs to return an empty set. This coding pattern is
common in a lot of managed languages, in particular with C# and Java.

When returning a zero-length array from a method, it’s more efficient to
return a pre-allocated static instance of the zero-length array than to
repeatedly create empty arrays.

## Use native arrays or other native containers for large arrays

Unity’s [garbage collector](performance-garbage-collector.html) is a heuristic
garbage collector, which means that it treats any field that has the size of a
pointer as if it is a pointer. The garbage collector checks every pointer and
reference that it encounters.

When you use large arrays (with more than 10 thousand elements), the garbage
collector might interpret large arrays as a long list of pointers that it
needs to check, which increases memory pressure and slows the garbage
collector down.

The scripting VM also has to allocate big chunks of managed heap space for
large arrays which increases the chance that a random value looks like a valid
address in the managed heap chunk’s memory address range. Large arrays are
also a big contributing factor to managed heap fragmentation.

If you need to allocate arrays of such length, consider using the collection
types in `Unity.Collections` namespace (including
[`NativeArray`](../ScriptReference/Unity.Collections.NativeArray_1.html)) in
the Unity core API, and the data structures in the [Unity Collections
package](https://docs.unity3d.com/Packages/com.unity.collections@latest). As
an additional benefit, using these collections are compatible with the [job
system](job-system.html) and Burst.

## Additional resources

  * [Managed memory introduction](performance-managed-memory-introduction.html)
  * [Reference type management](performance-reference-types.html)
  * [Creating reusable code](performance-reusable-code.html)

[](performance-reusable-code.html)

Using coding patterns with reusable memory

[](performance-native-memory.html)

Native memory

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

