def find_median(nums1, nums2):
    nums = nums1 + nums2
    len_t = len(nums)
    nums.sort()

    if len_t % 2 == 0:
        median = (nums[int(len_t/2) - 1] + nums[int(len_t/2)])/2
    else:
        median = nums[int(len_t/2)]

    return float(median)


def find_median2(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    len_t = len1 + len2
    i, j = 0, 0
    nums = []

    while i <= len1 or j <= len2:
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
            if i == len1:
                nums += nums2[j:]
                break
        else:
            nums.append(nums2[j])
            j += 1
            if j == len2:
                nums += nums1[i:]
                break
        if int(i + j) > int(len_t/2):
            break

    if len_t % 2 == 0:
        median = (nums[int(len_t / 2) - 1] + nums[int(len_t / 2)]) / 2
    else:
        median = nums[int(len_t / 2)]

    return find_median


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median2(nums1, nums2))
    # print(find_median(nums1, nums2))
